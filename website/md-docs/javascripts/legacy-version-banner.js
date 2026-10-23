// Shows a notice above the page content when the version being viewed is
// the development build ("dev") or anything other than the one mike aliases
// as "latest". The version is worked out at runtime from the URL and mike's
// versions.json rather than from per-version config, so every version can
// ship the same mkdocs.yml (main is a straight copy of the release branch).
// Material doesn't expose `extra` in #__config, so config can't drive this.

const DEV_VERSION = "dev";
const LATEST_ALIAS = "latest";

function getSiteConfig() {
  const configNode = document.querySelector("#__config");
  if (!configNode) return null;

  try {
    return JSON.parse(configNode.textContent || "{}");
  } catch {
    return null;
  }
}

function getVersionRoot(config) {
  // config.base is the relative path from this page to the version root,
  // e.g. "../.." -- resolving it against the page URL gives /<version>/.
  const base = config?.base;
  if (typeof base !== "string") return null;
  return new URL(base.endsWith("/") ? base : `${base}/`, window.location.href);
}

async function loadVersions(siteRoot) {
  try {
    const response = await fetch(new URL("versions.json", siteRoot));
    if (!response.ok) return null;
    const versions = await response.json();
    return Array.isArray(versions) ? versions : null;
  } catch {
    return null;
  }
}

function buildBanner({ label, message, linkText, linkHref }) {
  const banner = document.createElement("aside");
  banner.className = "legacy-version-banner";
  banner.setAttribute("role", "note");
  banner.setAttribute("aria-label", label);

  const labelNode = document.createElement("p");
  labelNode.className = "legacy-version-banner__label";
  labelNode.textContent = label;

  const messageNode = document.createElement("p");
  messageNode.className = "legacy-version-banner__message";
  messageNode.textContent = `${message} `;

  if (linkHref) {
    const link = document.createElement("a");
    link.href = linkHref;
    link.textContent = linkText;
    messageNode.appendChild(link);
  }

  banner.appendChild(labelNode);
  banner.appendChild(messageNode);
  return banner;
}

async function mountVersionBanner() {
  const container = document.querySelector(".md-content__inner");
  if (!container || container.querySelector(".legacy-version-banner")) return;

  const versionRoot = getVersionRoot(getSiteConfig());
  if (!versionRoot) return;

  // Not served through mike (e.g. plain `mkdocs serve`): no versions.json
  // one level up, so no banner.
  const siteRoot = new URL("../", versionRoot);
  const versions = await loadVersions(siteRoot);
  if (!versions) return;

  const segment = decodeURIComponent(versionRoot.pathname.split("/").filter(Boolean).pop() || "");
  const current = versions.find(
    (entry) => entry.version === segment || (entry.aliases || []).includes(segment),
  );
  if (!current) return;

  const latest = versions.find((entry) => (entry.aliases || []).includes(LATEST_ALIAS));
  const latestHref = latest ? new URL(`${LATEST_ALIAS}/`, siteRoot).href : null;
  const latestTitle = latest?.title || latest?.version;

  let banner = null;
  if (current.version === DEV_VERSION) {
    banner = buildBanner({
      label: "Development version",
      message:
        "These docs track EdgeTX development and may describe features or changes that are not in a released version yet.",
      linkText: latest ? `View the ${latestTitle} release docs.` : "",
      linkHref: latestHref,
    });
  } else if (latest && current.version !== latest.version) {
    banner = buildBanner({
      label: "Legacy version",
      message: `You are viewing the documentation for EdgeTX ${current.title || current.version}. It is kept for reference and may not include later corrections.`,
      linkText: `Go to the latest version (${latestTitle}).`,
      linkHref: latestHref,
    });
  }

  if (banner && !container.querySelector(".legacy-version-banner")) {
    container.insertBefore(banner, container.firstChild);
  }
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", mountVersionBanner, { once: true });
} else {
  mountVersionBanner();
}
