# loadScript

`loadScript(path [, mode [, env]])`

Load and compile a Lua script from the SD card.

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `path` | yes | `string` | Script file path. |
| `mode` | no | `string` | Compilation mode. |
| `env` | no | `table` | Custom environment table. |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `chunk` | `function|nil` | Compiled Lua chunk when loading succeeds. |
| `errmsg` | `string|nil` | Error message when loading fails. |

## Availability

- Since: `2.2.0`
- Radio support: `all`

## Source

`radio/src/lua/api_general.cpp`

## Enrichment

The sections below are authored outside the firmware source so examples, compatibility notes, and learning material can evolve without bloating C++ API comments.

## Extended Description

`loadScript` should eventually include examples showing how to load reusable Lua modules and how to handle `nil, errmsg` error returns cleanly.

## Examples

```lua
local chunk, errmsg = loadScript("/SCRIPTS/TOOLS/demo.lua")
if not chunk then
  return errmsg
end

local mod = chunk()
```
