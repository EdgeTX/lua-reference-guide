## Extended Description

`getVersion` is a good example of the split between source-owned API truth and docs-owned enrichment. The function signature, return values, and availability belong in upstream source annotations. Cross-version guidance and worked examples belong here.

## Examples

This example shows the multi-value form used in modern EdgeTX releases such as `2.4.0`:

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

Use the overlay for return-shape clarification and examples without expanding the firmware source comment.

## Additional Learning

Teaching videos, simulator captures, or short migration walkthroughs for `getVersion` should live here rather than in the firmware source tree.
