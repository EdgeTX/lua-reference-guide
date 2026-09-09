## Extended Description

`loadScript` fills a similar role to Lua's `loadfile()`, but it adds EdgeTX-specific handling for `.lua` and `.luac` files. On radio targets, that usually means better load-time performance and lower runtime overhead when a compiled version is available.

Use the short summary from source annotations as the API-level definition. Keep the deeper usage guidance here, where it can evolve without expanding the firmware-source comment block.

Typical reasons to use `loadScript` directly:

- load reusable helper modules from the SD card
- control whether text or precompiled bytecode is preferred
- handle `nil, errmsg` returns explicitly when a script is missing or invalid

## Examples

```lua
local chunk, errmsg = loadScript("/SCRIPTS/TOOLS/demo.lua")
if not chunk then
  return errmsg
end

local mod = chunk()
```
