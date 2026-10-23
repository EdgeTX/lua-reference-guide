# model.setTimer

`model.setTimer(timer, value)`

Set model timer parameters

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `timer` | yes | `integer` | timer index (0 for Timer 1) |
| `value` | yes | `unknown` | timer parameters, see model.getTimer() |

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
