# model.getTimer

`model.getTimer(timer)`

Get model timer parameters

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `timer` | yes | `integer` | timer index (0 for Timer 1) |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `-` | `nil` | requested timer does not exist |
| `-` | `table` | timer parameters: * `mode` (number) timer trigger source: off, abs, stk,  stk%, sw/!sw, !m_sw/!m_sw  * `start` (number) start value [seconds], 0 for up timer, 0> down timer  * `value` (number) current value [seconds]  * `countdownBeep` (number) countdown beep (0­ = silent, 1 =­ beeps, 2­ = voice)  * `minuteBeep` (boolean) minute beep  * `persistent` (number) persistent timer  * `name` (string) timer name  * `showElapsed` (boolean) show elapsed |

## Availability

- Since: `2.0.0`
- Radio support: `all`

## Source

`radio/src/lua/api_model.cpp`
