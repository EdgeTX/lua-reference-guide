# accessTelemetryPush

`accessTelemetryPush()`

This functions allows for sending SPORT / ACCESS telemetry data toward the receiver,
and more generally, to anything connected SPORT bus on the receiver or transmitter.

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `module` | yes | `integer` | module index (0 = internal, 1 = external) |
| `rxUid` | yes | `integer` | receiver index |
| `sensorId` | yes | `unknown` | physical sensor ID |
| `frameId` | yes | `unknown` | frame ID |
| `dataId` | yes | `unknown` | data ID |
| `value` | yes | `unknown` | value |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `-` | `boolean` | data queued in output buffer or not. |

## Availability

- Since: `2.3`
- Radio support: `all`

## Notes

- When called without parameters, it will only return the status of the output buffer without sending anything.

## Source

`radio/src/lua/api_general.cpp`
