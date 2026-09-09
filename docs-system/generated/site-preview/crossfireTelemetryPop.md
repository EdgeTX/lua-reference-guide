# crossfireTelemetryPop

`crossfireTelemetryPop()`

Pops a received Crossfire Telemetry packet from the queue.

## Parameters

None.

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `-` | `nil` | queue does not contain any (or enough) bytes to form a whole packet |
| `command` | `integer` |  |
| `packet` | `table` | data bytes |

## Availability

- Since: `2.2.0`
- Radio support: `all`

## Source

`radio/src/lua/api_general.cpp`
