# model.getCustomFunction

`model.getCustomFunction(function)`

Get Custom Function parameters

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `function` | yes | `integer` | custom function number (use 0 for CF1) |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `-` | `nil` | requested custom function does not exist |
| `-` | `table` | custom function data: * `switch` (number) switch index  * `func` (number) function index  * `name` (string)  Name of track to play (only returned only returned if action is play track, sound or script)  * `value` (number) value (only returned only returned if action is **not** play track, sound or script)  * `mode` (number) mode (only returned only returned if action is **not** play track, sound or script)  * `param` (number) parameter (only returned only returned if action is **not** play track, sound or script)  * `active` (number) 0 = disabled, 1 = enabled  * `repetition` (number) -1 to 60, range and meaning depend on function |

## Availability

- Since: `2.0.0`
- Radio support: `all`

## Source

`radio/src/lua/api_model.cpp`
