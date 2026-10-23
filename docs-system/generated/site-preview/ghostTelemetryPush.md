# ghostTelemetryPush

`ghostTelemetryPush()`

This functions allows for sending telemetry data toward the Ghost link.

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `command` | yes | `unknown` | command |
| `data` | yes | `table` | table of data bytes |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `-` | `boolean` | data queued in output buffer or not. |
| `-` | `nil` | incorrect telemetry protocol. |

## Availability

- Since: `2.7.0`
- Radio support: `all`

## Notes

- When called without parameters, it will only return the status of the output buffer without sending anything.

## Source

`radio/src/lua/api_general.cpp`
