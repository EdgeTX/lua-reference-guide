# model.setGlobalVariable

`model.setGlobalVariable(index, flight_mode, value)`

Sets current global variable value. See also model.getGlobalVariable()

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `index` | yes | `integer` | zero based global variable index, use 0 for GV1, 8 for GV9 |
| `flight_mode` | yes | `integer` | Flight mode number (0 = FM0, 8 = FM8) |
| `value` | yes | `unknown` | new value for global variable. Permitted range is from -1024 to 1024. |

## Returns

None.

## Availability

- Since: `unknown`
- Radio support: `all`

## Notes

- Global variable can only store integer values,
any floating point value is converted into integer value
by truncating everything behind a floating point.

## Source

`radio/src/lua/api_model.cpp`
