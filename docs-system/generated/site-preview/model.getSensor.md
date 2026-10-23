# model.getSensor

`model.getSensor(sensor)`

Get Telemetry Sensor parameters

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `sensor` | yes | `integer` | sensor number (use 0 for sensor 1) |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `-` | `nil` | requested sensor does not exist |
| `-` | `table` | with sensor data: * `type` (number) 0 = custom, 1 = calculated  * `name` (string) Name  * `unit` (number) See list of units in the appendix of the OpenTX Lua Reference Guide  * `prec` (number) Number of decimals  * `id`   (number) Only custom sensors  * `instance` (number) Only custom sensors  * `formula` (number) Only calculated sensors. 0 = Add etc. see list of formula choices in Companion popup |

## Availability

- Since: `2.3.0`
- Radio support: `all`

## Source

`radio/src/lua/api_model.cpp`
