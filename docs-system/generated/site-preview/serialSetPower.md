# serialSetPower

`serialSetPower(port_nr, value)`



## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `port_nr` | yes | `valid` | values are only 0 and 1 on radios that have SWSERIALPOWER defined 0 - first serial port, e.g. on TX16S AUX1                 1 - second serial port, e.g. on TX16S AUX2 |
| `value` | yes | `0` | - disable power 1 - enable power |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `success` | `true/false` | . |

## Availability

- Since: `2.9.0`
- Radio support: `all`

## Source

`radio/src/lua/api_general.cpp`
