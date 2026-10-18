# getRSSI

`getRSSI()`

Get RSSI value as well as low and critical RSSI alarm levels (in dB)

## Parameters

None.

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `rssi` | `unknown` | RSSI value (0 if no link) |
| `alarm_low` | `unknown` | Configured low RSSI alarm level |
| `alarm_crit` | `unknown` | Configured critical RSSI alarm level |

## Availability

- Since: `2.2.0`
- Radio support: `all`

## Source

`radio/src/lua/api_general.cpp`
