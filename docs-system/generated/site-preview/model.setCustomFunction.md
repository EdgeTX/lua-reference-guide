# model.setCustomFunction

`model.setCustomFunction(function, value)`

Set Custom Function parameters

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `function` | yes | `integer` | custom function number (use 0 for CF1) |
| `value` | yes | `table` | custom function parameters, see model.getCustomFunction() for table format |

## Returns

None.

## Availability

- Since: `2.0.0`
- Radio support: `all`

## Notes

- If a parameter is missing from the value, then
that parameter remains unchanged.

## Source

`radio/src/lua/api_model.cpp`
