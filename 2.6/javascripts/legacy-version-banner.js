// Loader for the version banner. The banner itself (logic and wording) lives
// in version-banner.js, and every version loads the copy published under
// /latest/, so it can be changed in one place, on the latest release branch,
// instead of on every docs branch. If that copy can't be loaded (e.g. a site
// not served through mike), this version's own copy is used instead.
(() => {
  let base;
  try {
    base = JSON.parse(document.querySelector("#__config")?.textContent || "{}").base;
  } catch {
    return;
  }
  if (typeof base !== "string") return;

  // config.base is the relative path from this page to the version root.
  const versionRoot = new URL(base.endsWith("/") ? base : `${base}/`, window.location.href);
  const sources = [
    new URL("../latest/javascripts/version-banner.js", versionRoot),
    new URL("javascripts/version-banner.js", versionRoot),
  ];

  const load = (index) => {
    if (index >= sources.length) return;
    const script = document.createElement("script");
    script.src = sources[index].href;
    script.onerror = () => {
      script.remove();
      load(index + 1);
    };
    document.head.appendChild(script);
  };

  load(0);
})();
