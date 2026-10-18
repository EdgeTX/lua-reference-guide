# EdgeTX Lua Docs Migration Plan

## Summary

This project will move away from GitBook and rebuild the Lua API documentation flow around the EdgeTX source code. The long-term source of truth for API syntax, parameters, return values, availability, and practical typing will live in the official EdgeTX code repository, not in this docs repository.

The first published output of the new system will be the EdgeTX 2.12 documentation set. However, the annotation model and source cleanup work should start in the current upstream EdgeTX codebase, then be backported or adapted as needed for the 2.12 release line.

The new pipeline should generate two downstream products from the same extracted API data:

- Markdown API reference for the published docs site
- LuaLS `*.d.lua` definition files for autocomplete, inline documentation, and type checking

## Goals

- Make upstream code comments the single maintained source of truth for Lua API facts
- Stop relying on GitBook as the docs platform
- Generate API reference pages from source annotations
- Keep richer narrative content separate from generated API truth
- Support LuaLS generation from the same extracted model
- Publish EdgeTX 2.12 first using the new pipeline
- Use one unified MkDocs experience for all versions that are migrated to the new site
- Preserve old-version content when needed without recreating GitBook inside MkDocs

## Operating Model

### Upstream EdgeTX code repo

The official EdgeTX code repository is the authoritative source for:

- API symbol names
- syntax and signatures
- parameter definitions
- return values
- availability and version metadata
- implementation-coupled notes
- practical type information used for LuaLS

If API documentation truth is wrong or missing, it should be fixed there first through upstream PRs.

### This docs repo

This repository becomes a downstream consumer and publisher:

- extract API annotations from upstream source
- build normalized intermediate API data
- render Markdown reference pages
- render LuaLS definition files
- merge overlay content for richer docs
- publish a static docs site

This repo should not become a competing owner of API syntax truth.

## Docs Experience Policy

The migration will standardize on one docs platform and one presentation model for all versions that move onto the new site.

Rules:

- GitBook is treated as a legacy publishing system, not a design target to be recreated inside MkDocs
- EdgeTX 2.12 is the first release intended to publish from the new MkDocs pipeline
- Any older versions that are later imported into MkDocs should use the same MkDocs shell, navigation model, and version-switching behavior as newer versions
- Older versions may retain legacy content, known gaps, or historical wording, but should not require a separate GitBook-like theme inside MkDocs
- Content fixes remain branch-specific and are only applied to older release lines when explicitly backported or edited there
- Older versions should be published from their own branches or release refs, not copied into the 2.12 docs tree

This means the project preserves historical content where useful, but does not preserve GitBook presentation at all costs.

## Migration Strategy

### Phase 1: Normalize upstream source annotations

Review and improve Lua API comments in the current EdgeTX upstream codebase.

The new annotation format should cover:

- canonical API id
- module or namespace
- syntax or signature
- short summary
- parameters with names, required or optional state, and practical types
- return values with practical types
- availability metadata such as version introduced and radio or display support
- short implementation-specific notes when necessary

This phase should:

- inventory all Lua API entry points
- identify missing or inconsistent annotations
- normalize parameter naming and optional argument notation
- add practical type information where useful for LuaLS
- avoid placing long examples or heavy prose in source comments
- land the cleanup in upstream PRs

### Phase 2: Define extraction schema

Build a deterministic extractor that reads normalized upstream annotations and produces a versioned intermediate representation.

The intermediate model should include at least:

- `id`
- `symbol`
- `container` or `module`
- `kind`
- `syntax`
- `summary`
- `parameters`
- `returns`
- `availability`
- `notes`
- `types`
- `source_location`
- `upstream_ref`
- `docs_version`

The extractor should fail clearly on malformed annotations, duplicates, or missing required fields.

### Phase 3: Generate Markdown API reference

Use the intermediate model to generate API reference Markdown files.

Requirements:

- no hand editing of generated Markdown
- stable output for the same upstream input
- generated sections remain authoritative for API truth
- pages map cleanly into the final docs navigation

### Phase 4: Generate LuaLS definitions

Use the same intermediate model to generate LuaLS `*.d.lua` files.

The type fidelity target is practical editor usefulness, not a perfect formal type system. The generator should support:

- primitive Lua types
- optional parameters
- unions such as `integer|string`
- structured tables for stable inputs and return values
- constants and module namespaces

The existing `edgetx-lua-stdlib` repository should be treated as a strong reference for output shape and usability, but not as the long-term source of truth.

### Phase 5: Add overlay enrichment

Keep richer documentation outside generated source data.

Overlay files should be stored separately per API item and may contain:

- long descriptions
- examples
- related topics
- extended notes
- assets or screenshots if needed

Merge rules:

- generated syntax and core API metadata always win
- overlays add narrative content only
- missing overlays are valid

### Phase 6: Replace GitBook with MkDocs Material

Publish the docs as a static site using MkDocs Material.

The site should combine:

- generated API reference pages
- hand-authored guides and conceptual docs
- overlay-enriched sections where available

MkDocs replaces GitBook for:

- site rendering
- navigation
- search
- theming
- static publishing

The first supported MkDocs release is EdgeTX 2.12. Older releases may be added later, but if they are added they should adopt the same MkDocs presentation rather than a separate legacy theme.

### Phase 7: Unify versioned publishing

Publish documentation versions through one MkDocs and `mike` pipeline.

Requirements:

- each published docs version maps to a specific source branch or release ref
- `main` or equivalent development work publishes as a development version such as `dev`
- EdgeTX 2.12 becomes the first release alias promoted as `latest` when ready
- older versions such as 2.11 or 2.10 can be imported later as legacy-content versions
- imported legacy versions should display a small notice that the content is historical and may not include later corrections
- imported legacy versions should be built from their own branch content, not from duplicated copies stored under another version

**Status: done.** 2.4 through 2.11 are imported and published via `mike`, built from `tools/import_legacy_gitbook.py` against each version's own GitBook-era branch content (2.4-2.7 and 2.11 come from the upstream `EdgeTX/lua-reference-guide` repo, since this fork doesn't carry those branches). Deployed manually (`mike deploy --config-file ... --push` per version), not via `.github/workflows/publish-versioned-docs.yml` -- that workflow only handles `main`/`edgetx_2.12`, since the legacy branches don't exist in this fork for it to trigger from. `opentx_2.2`/`opentx_2.3` (pre-EdgeTX) were left out of scope.

Non-requirement:

- imported legacy versions do not need to match historical GitBook visuals

## Versioning Approach

Two tracks must be kept separate:

- current upstream EdgeTX main is where annotation quality and source format are improved first
- EdgeTX 2.12 is the first target documentation version to be published with the new pipeline

Important rule:

- release docs must always be generated from the matching release source ref

That means 2.12 docs and 2.12 LuaLS output must be generated from a 2.12-compatible upstream ref, not from current main. If needed, comment and annotation fixes from current main should be backported to the 2.12 code line.

Publishing policy:

- EdgeTX 2.12 is the first release line to publish on the new MkDocs site
- `main` may publish as `dev` for ongoing work before release
- pre-2.12 versions may remain on GitBook during transition
- if pre-2.12 versions are later migrated into MkDocs, their content should remain branch-specific but their presentation should use the shared MkDocs design
- no release branch should be changed implicitly by work done for another release branch
- older versions should be published from their own branches or release refs rather than copied into the 2.12 branch

Recommended rollout:

1. Finish the MkDocs design, generation flow, and version-switching behavior on `2.12` and `dev`
2. Publish `2.12` as the first release on the new site
3. Decide whether older versions need to be imported into MkDocs immediately or can remain on GitBook temporarily
4. If older versions are imported, mark them as legacy content with a banner instead of recreating GitBook styling
5. Retire GitBook once the MkDocs versioned site is sufficiently complete

## Implementation Plan

The migration implementation should be executed in ordered workstreams so the first shippable outcome is a working EdgeTX 2.12 docs site published from MkDocs.

### Workstream 1: Lock the 2.12 site shell

Scope:

- finalize `mkdocs.yml` structure
- finalize theme, branding, navigation, and version-switcher behavior
- define the shared page layout for generated API pages and hand-authored guides
- define the legacy-version banner pattern for older branches that may later be imported

Done when:

- the 2.12 site builds locally without structural blockers
- key navigation sections are stable
- the site theme is accepted as the shared MkDocs UI for all migrated versions

### Workstream 2: Finish pipeline outputs for 2.12

Scope:

- finalize extraction schema and generator behavior
- generate Markdown API reference pages from a pinned 2.12-compatible upstream ref
- generate LuaLS definition files from the same input
- define which parts of the docs are generated versus hand-authored overlays

Done when:

- generated API docs are reproducible
- LuaLS output is generated from the same API model
- overlay merge rules are working and documented by example

### Workstream 3: Prepare branch-based version publishing

Scope:

- update the publishing workflow for `edgetx_2.12`
- keep `main` publishing as `dev`
- confirm version ids, aliases, and `latest` promotion rules
- confirm that each version is built from its own branch or release ref

Done when:

- `main` publishes as `dev`
- `edgetx_2.12` publishes as the release version for 2.12
- the release version can be promoted to `latest` when ready
- no version relies on copied content from another branch

### Workstream 4: Validate the 2.12 release candidate

Scope:

- verify local builds
- verify generated docs links, navigation, and grouping
- verify search behavior and page discoverability
- verify representative LuaLS definitions against expected editor usefulness
- review warnings and fix the highest-value blockers

Done when:

- local preview is usable for day-to-day review
- major docs sections render correctly
- high-value broken links and nav issues are resolved or explicitly accepted
- the 2.12 site is good enough to publish as the first MkDocs release

### Workstream 5: Decide legacy-version migration timing

**Status: done.** 2.4 through 2.11 are imported into MkDocs and published via `mike`, each from its own branch content with the legacy-version notice enabled. See the note under "Versioning Approach" above for how. `opentx_2.2`/`opentx_2.3` were left on their own (pre-EdgeTX, not part of this migration).

## Immediate Execution Order

The recommended order of implementation is:

1. Finish the shared MkDocs site shell for `2.12`
2. Finish the 2.12 extraction and generation pipeline outputs
3. Update the publish workflow to support `edgetx_2.12`, `dev`, and `latest`
4. Validate the complete 2.12 site locally
5. Publish 2.12 as the first MkDocs release
6. ~~Revisit whether 2.11 and older should remain on GitBook or be imported later~~ -- done, see Workstream 5

## First Actionable Tasks

- finalize `mkdocs.yml` and shared site assets for the 2.12 UI
- verify generated API pages are correctly wired into navigation
- add `edgetx_2.12` publishing support to the GitHub Actions workflow
- define the exact alias rule for promoting 2.12 to `latest`
- add a reusable legacy-version notice for future older-version imports
- collect and prioritize current MkDocs build warnings into fix now versus defer

## LuaLS Considerations

LuaLS should be a first-class output of the new system, not an afterthought.

The upstream annotation contract must carry enough structured information to support:

- editor autocomplete
- inline documentation
- type checking
- module and constant discovery

The recommended type strategy is practical typing:

- be precise where the API is stable and clear
- use structured table types where the interface is well defined
- use broader types where behavior is dynamic or uncertain
- avoid inventing precision that is not justified by the implementation

## Testing And Validation

The migration should include the following validation steps:

- confirm all exported Lua API entries in the upstream codebase have valid annotations
- validate the extractor against malformed and incomplete annotations
- generate Markdown docs from a pinned 2.12 upstream ref
- generate LuaLS files from the same pinned 2.12 upstream ref
- compare generated 2.12 docs against the current published 2.12 docs
- compare generated LuaLS output against the current `edgetx-lua-stdlib` structure and coverage
- verify output is stable across repeated runs
- verify overlay merge keeps generated API truth authoritative
- verify MkDocs builds the combined site successfully

## Non-Goals For First Version

- generating tutorials or conceptual guides from code
- using AI as a required part of the build pipeline
- making this docs repo the owner of API truth
- building a custom docs web app instead of using a static docs framework

## Defaults And Assumptions

- The official EdgeTX source repository is upstream and authoritative
- This repository is downstream and publishes generated outputs
- EdgeTX 2.12 is the first release line to publish through the new system
- GitBook will be replaced rather than reimplemented inside MkDocs
- A unified MkDocs design is preferred over preserving historical GitBook styling
- Older versions may remain temporarily on GitBook during transition, but migrated versions should share the MkDocs UI
- AI may help draft overlay content, but only as an optional reviewed workflow
- LuaLS generation is part of the intended final architecture
