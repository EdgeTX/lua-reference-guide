# getDateTime

`getDateTime()`

Return current system date and time that is kept by the RTC unit

## Parameters

None.

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `-` | `table` | current date and time, table elements: * `year` (number) year  * `mon` (number) month  * `day` (number) day of month  * `hour` (number) hours  * `hour12` (number) hours in US format  * `min` (number) minutes  * `sec` (number) seconds  * `suffix` (text) am or pm |

## Availability

- Since: `unknown`
- Radio support: `all`

## Source

`radio/src/lua/api_general.cpp`
