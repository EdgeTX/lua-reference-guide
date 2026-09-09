function getSiteConfig() {
  const configNode = document.querySelector("#__config");
  if (!configNode) return null;

  try {
    return JSON.parse(configNode.textContent || "{}");
  } catch {
    return null;
  }
}

function mountLegacyVersionBanner() {
  const config = getSiteConfig();
  const legacyConfig = config?.extra?.legacy_version;
  if (!legacyConfig?.enabled) return;

  const container = document.querySelector(".md-content__inner");
  if (!container || container.querySelector(".legacy-version-banner")) return;

  const banner = document.createElement("aside");
  banner.className = "legacy-version-banner";
  banner.setAttribute("role", "note");
  banner.setAttribute("aria-label", legacyConfig.label || "Legacy version");

  const label = document.createElement("p");
  label.className = "legacy-version-banner__label";
  label.textContent = legacyConfig.label || "Legacy version";

  const message = document.createElement("p");
  message.className = "legacy-version-banner__message";
  message.textContent =
    legacyConfig.message ||
    "This documentation version is preserved for reference and may not include later corrections or the newest docs structure.";

  banner.appendChild(label);
  banner.appendChild(message);
  container.insertBefore(banner, container.firstChild);
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", mountLegacyVersionBanner, { once: true });
} else {
  mountLegacyVersionBanner();
}
