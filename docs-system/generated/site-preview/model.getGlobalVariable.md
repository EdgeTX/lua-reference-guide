# model.getGlobalVariable

`model.getGlobalVariable(index, flight_mode)`

Return current global variable value

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `index` | yes | `integer` | zero based global variable index, use 0 for GV1, 8 for GV9 |
| `flight_mode` | yes | `integer` | Flight mode number (0 = FM0, 8 = FM8) |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `-` | `nil` | requested global variable does not exist |
| `-` | `integer` | current value of global variable |

## Availability

- Since: `unknown`
- Radio support: `all`

## Notes

- a simple warning or notice

## Source

`radio/src/lua/api_model.cpp`
