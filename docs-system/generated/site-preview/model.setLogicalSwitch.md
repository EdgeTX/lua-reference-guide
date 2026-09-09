# model.setLogicalSwitch

`model.setLogicalSwitch(switch, value)`

Set Logical Switch parameters

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `switch` | yes | `integer` | logical switch number (use 0 for LS1) |
| `value` | yes | `table` | see model.getLogicalSwitch() for table format |

## Returns

None.

## Availability

- Since: `2.0.0`
- Radio support: `all`

## Notes

- If a parameter is missing from the value, then
that parameter remains unchanged.
- To set the `and` member (which is Lua keyword)
use the following syntax: `model.setLogicalSwitch(30, {func=4,v1=1,v2=-99, ["and"]=24})`

## Source

`radio/src/lua/api_model.cpp`
