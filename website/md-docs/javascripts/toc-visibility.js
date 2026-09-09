function updateTocVisibility() {
  const sidebar = document.querySelector('.md-sidebar--secondary[data-md-type="toc"]');
  const tocList = sidebar?.querySelector('.md-nav--secondary [data-md-component="toc"]');
  const hasItems = Boolean(tocList?.querySelector(".md-nav__item"));

  if (!sidebar) return;

  sidebar.hidden = !hasItems;
}

if (typeof document$ !== "undefined") {
  document$.subscribe(updateTocVisibility);
} else if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", updateTocVisibility, { once: true });
} else {
  updateTocVisibility();
}
