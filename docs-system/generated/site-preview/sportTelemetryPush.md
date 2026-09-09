# sportTelemetryPush

`sportTelemetryPush()`

This functions allows for sending SPORT telemetry data toward the receiver,
and more generally, to anything connected SPORT bus on the receiver or transmitter.

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `sensorId` | yes | `unknown` | physical sensor ID |
| `frameId` | yes | `unknown` | frame ID |
| `dataId` | yes | `unknown` | data ID |
| `value` | yes | `unknown` | value |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `-` | `boolean` | data queued in output buffer or not. |
| `-` | `nil` | incorrect telemetry protocol. |

## Availability

- Since: `2.2.0`
- Radio support: `all`

## Notes

- When called without parameters, it will only return the status of the output buffer without sending anything.

## Source

`radio/src/lua/api_general.cpp`
