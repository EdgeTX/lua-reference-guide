# Annotation Contract

The long-term annotation contract belongs in the upstream EdgeTX code repository.

The generator introduced in this repository expects the source model to provide:

- canonical API id
- current symbol name
- module or global namespace
- kind such as `function`
- syntax
- short summary
- parameters with names, required state, and practical types
- return values with practical types
- availability metadata
- source location

Anything narrative-heavy should stay out of the source annotation layer and be added through overlays instead.

## Recommended Split

Keep this in upstream code annotations:

- canonical syntax and signature
- one short summary sentence
- parameters and practical types
- return values and practical types
- version and availability
- short implementation-coupled notices only

Keep this in downstream overlays:

- examples
- compatibility notes
- rename and deprecation guidance
- longer explanations
- multi-paragraph descriptions
- lists and comparison tables
- screenshots
- teaching videos
- related topics
- workflow guidance

## Enforcement In This Repo

The extractor only promotes:

- the first summary paragraph
- tagged API facts such as `@param`, `@retval`, `@status`, and `@notice`

Unstructured rich prose such as extra paragraphs, lists, tables, and fenced examples should move to overlays instead of being embedded in C++ comments.

## Stable Docs Identity

The docs pipeline may assign a stable `doc_id` outside the C++ source tree.

That `doc_id` is the long-lived identity for:

- overlay lookup
- generated page paths
- future symbol renames and deprecations

The upstream source annotation should continue to expose only the actual callable symbol and syntax.
