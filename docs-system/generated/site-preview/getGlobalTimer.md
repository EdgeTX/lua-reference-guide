# getGlobalTimer

`getGlobalTimer()`

Returns radio timers

## Parameters

None.

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `-` | `table` | with elements: * `gtimer` (number) radio global timer in seconds * `session` (number) radio session in seconds * `ttimer` (number) radio throttle timer in seconds * `tptimer` (number) radio throttle percent timer in seconds |

## Availability

- Since: `unknown`
- Radio support: `all`

## Source

`radio/src/lua/api_general.cpp`
