const DECISION_SERVER = "http://127.0.0.1:8123";
const LOCAL_STORAGE_KEY = "lua-review-decisions";

function loadLocalDecisions() {
  try {
    return JSON.parse(window.localStorage.getItem(LOCAL_STORAGE_KEY) || "{}");
  } catch {
    return {};
  }
}

function defaultTypeOptions() {
  return {
    common_types: [
      "TODO",
      "integer",
      "number",
      "string",
      "boolean",
      "table",
      "function",
      "pointer",
      "nil",
      "integer|string",
      "table|nil",
      "function|nil",
      "string|nil",
    ],
    custom_types: [],
  };
}

function saveLocalDecisions(decisions) {
  window.localStorage.setItem(LOCAL_STORAGE_KEY, JSON.stringify(decisions));
}

async function fetchServerDecisions() {
  const response = await fetch(`${DECISION_SERVER}/decisions`);
  if (!response.ok) {
    throw new Error(`decision server returned ${response.status}`);
  }
  return response.json();
}

async function fetchTypeOptions() {
  const response = await fetch(`${DECISION_SERVER}/types`);
  if (!response.ok) {
    throw new Error(`types server returned ${response.status}`);
  }
  return response.json();
}

async function saveServerDecision(itemId, payload) {
  const response = await fetch(`${DECISION_SERVER}/decisions/save`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ item_id: itemId, ...payload }),
  });
  if (!response.ok) {
    throw new Error(`decision save failed with ${response.status}`);
  }
  return response.json();
}

function mergedTypeOptions(serverTypes) {
  const base = defaultTypeOptions();
  const combined = [...base.common_types];
  const seen = new Set(combined);
  for (const typeName of serverTypes?.custom_types || []) {
    if (!seen.has(typeName)) {
      combined.push(typeName);
      seen.add(typeName);
    }
  }
  return combined;
}

function populateTypeOptions(panel, options) {
  panel.querySelectorAll("select").forEach((select) => {
    const current = select.dataset.currentType || select.value || "TODO";
    select.innerHTML = "";
    options.forEach((option) => {
      const optionEl = document.createElement("option");
      optionEl.value = option;
      optionEl.textContent = option;
      select.appendChild(optionEl);
    });
    if (options.includes(current)) {
      select.value = current;
    } else {
      select.value = "TODO";
    }
  });
}

function panelChoices(panel) {
  const params = {};
  const returns = {};
  panel.querySelectorAll("select").forEach((select) => {
    const value = select.value;
    const fieldKind = select.dataset.fieldKind;
    const fieldName = select.dataset.fieldName;
    const customInput = panel.querySelector(
      `input[data-custom-type="true"][data-field-kind="${fieldKind}"][data-field-name="${CSS.escape(fieldName)}"]`,
    );
    const customValue = customInput?.value?.trim();
    const chosenValue = customValue || value;
    if (!chosenValue || chosenValue === "TODO") {
      return;
    }
    if (fieldKind === "param") {
      params[fieldName] = chosenValue;
    } else {
      returns[fieldName] = chosenValue;
    }
  });
  return { params, returns };
}

function applySavedChoices(panel, saved) {
  panel.querySelectorAll("select").forEach((select) => {
    const fieldKind = select.dataset.fieldKind;
    const fieldName = select.dataset.fieldName;
    const value = fieldKind === "param"
      ? saved?.params?.[fieldName]
      : saved?.returns?.[fieldName];
    if (value) {
      const optionValues = Array.from(select.options).map((option) => option.value);
      const customInput = panel.querySelector(
        `input[data-custom-type="true"][data-field-kind="${fieldKind}"][data-field-name="${CSS.escape(fieldName)}"]`,
      );
      if (optionValues.includes(value)) {
        select.value = value;
        if (customInput) {
          customInput.value = "";
        }
      } else {
        select.value = "TODO";
        if (customInput) {
          customInput.value = value;
        }
      }
    }
  });
}

async function initDecisionPanels() {
  const localDecisions = loadLocalDecisions();
  let serverDecisions = {};
  let serverOnline = false;
  let typeOptions = defaultTypeOptions();

  try {
    serverDecisions = await fetchServerDecisions();
    serverOnline = true;
  } catch {
    serverOnline = false;
  }

  try {
    typeOptions = await fetchTypeOptions();
  } catch {
    typeOptions = defaultTypeOptions();
  }

  document.querySelectorAll(".decision-panel").forEach((panel) => {
    const itemId = panel.dataset.itemId;
    const status = panel.querySelector('[data-role="status"]');
    populateTypeOptions(panel, mergedTypeOptions(typeOptions));
    const saved = serverDecisions[itemId] || localDecisions[itemId] || {};
    applySavedChoices(panel, saved);
    status.textContent = serverOnline
      ? "Decision server connected. Selections will be saved for Codex."
      : "Decision server offline. Selections are only stored in this browser until the local save service starts.";

    const save = async () => {
      const choices = panelChoices(panel);
      localDecisions[itemId] = choices;
      saveLocalDecisions(localDecisions);
      if (serverOnline) {
        try {
          await saveServerDecision(itemId, choices);
          status.textContent = "Saved to docs-system/generated/review-decisions.json";
        } catch {
          status.textContent = "Save to server failed. Kept locally in this browser.";
        }
      } else {
        status.textContent = "Saved locally in this browser.";
      }
    };

    panel.querySelectorAll("select").forEach((select) => {
      select.addEventListener("change", save);
    });
    panel.querySelectorAll('input[data-custom-type="true"]').forEach((input) => {
      input.addEventListener("change", save);
      input.addEventListener("blur", save);
    });
    const saveButton = panel.querySelector('[data-role="save"]');
    if (saveButton) {
      saveButton.addEventListener("click", save);
    }
  });
}

document.addEventListener("DOMContentLoaded", initDecisionPanels);
