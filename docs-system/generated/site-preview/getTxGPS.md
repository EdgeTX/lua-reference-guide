# getTxGPS

`getTxGPS()`

Return the internal GPS position or nil if no valid hardware found

## Parameters

None.

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `-` | `table` | representing the current radio position * `lat` (number) internal GPS latitude, positive is North  * `lon` (number) internal GPS longitude, positive is East  * `numsat` (number) current number of sats locked in by the GPS sensor  * `fix` (boolean) fix status  * `alt` (number) internal GPS altitude in 0.1m  * `speed` (number) internal GPSspeed in 0.1m/s  * `heading`  (number) internal GPS ground course estimation in degrees * 10  * `hdop` (number)  internal GPS horizontal dilution of precision |

## Availability

- Since: `2.2.2`
- Radio support: `all`

## Source

`radio/src/lua/api_general.cpp`
