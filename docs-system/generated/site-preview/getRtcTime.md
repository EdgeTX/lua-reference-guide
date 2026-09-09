# getRtcTime

`getRtcTime()`

Return current RTC system date as unix timstamp (in seconds since 1. Jan 1970)

## Parameters

None.

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `-` | `integer` | Number of seconds elapsed since 1. Jan 1970 |

## Availability

- Since: `unknown`
- Radio support: `all`

## Notes

- Please note the RTC timestamp is kept internally as a 32bit integer, which will overflow
in 2038.

## Source

`radio/src/lua/api_general.cpp`
