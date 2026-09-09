# serialGetPower

`serialGetPower(port_nr)`



## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `port_nr` | yes | `valid` | values are only 0 and 1 on radios that have SWSERIALPOWER defined 0 - first serial port, e.g. on TX16S AUX1                 1 - second serial port, e.g. on TX16S AUX2 |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `value` | `true` | for power enabled, false for power disabled. |
| `-` | `nil` | the serial port power control not available on this radio |

## Availability

- Since: `2.9.0`
- Radio support: `all`

## Source

`radio/src/lua/api_general.cpp`
