# model.getLogicalSwitch

`model.getLogicalSwitch(switch)`

Get Logical Switch parameters

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `switch` | yes | `integer` | logical switch number (use 0 for LS1) |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `-` | `nil` | requested logical switch does not exist |
| `-` | `table` | logical switch data: * `func` (number) function index  * `v1` (number) V1 value (index)  * `v2` (number) V2 value (index or value)  * `v3` (number) V3 value (index or value)  * `and` (number) AND switch index  * `delay` (number) delay (time in 1/10 s)  * `duration` (number) duration (time in 1/10 s)  * `state` (boolean) current state of the logical switch  * `persistent` (boolean) if true then the state is persistent across reboot of the radio |

## Availability

- Since: `2.0.0`
- Radio support: `all`

## Source

`radio/src/lua/api_model.cpp`
