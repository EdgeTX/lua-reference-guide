# killEvents

`killEvents(key)`

Stops key state machine. See [Key Events](../key_events.md) for the detailed description.

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `key` | yes | `integer` | key to be killed, can also include event type (only the key part is used) |

## Returns

None.

## Availability

- Since: `2.0.0`
- Radio support: `all`

## Source

`radio/src/lua/api_general.cpp`
