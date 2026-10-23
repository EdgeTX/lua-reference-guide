# getVersionInfo

`getVersionInfo()`

Return the firmware version and platform details.

## Aliases

- `getVersion` (deprecated alias)

## Parameters

None.

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `version` | `string` | Version string. |
| `radio` | `string` | Radio or simulator identifier. |

## Availability

- Since: `2.4.0`
- Radio support: `all`

## Source

`radio/src/lua/api_general.cpp`

## Enrichment

The sections below are authored outside the firmware source so examples, compatibility notes, and learning material can evolve without bloating C++ API comments.

## Extended Description

`runtime.get-version` keeps one docs page even if the preferred callable name changes over time. The generated API truth shows the current symbol, while older names remain documented here as compatibility guidance.

## Examples

This example also runs in OpenTX versions where the function returned only one value:

```lua
local function run(event)
  local ver, radio, maj, minor, rev, osname = getVersion()
  print("version: "..ver)
  if radio then print("radio: "..radio) end
  if maj then print("maj: "..maj) end
  if minor then print("minor: "..minor) end
  if rev then print("rev: "..rev) end
  if osname then print("osname: "..osname) end
  return 1
end

return { run=run }
```

Output of the above script in simulator:

```text
version: 2.4.0
radio: tx16s-simu
maj: 2
minor: 4
rev: 0
osname: EdgeTX
```

## Compatibility Notes

During a rename window, keep the current preferred symbol in generated API metadata and list older callable names as deprecated aliases. This lets the page stay stable while users still find the old name.
