# model.deleteMix

`model.deleteMix(channel, line)`

Delete mixer line from specified Channel

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `channel` | yes | `integer` | channel number (use 0 for CH1) |
| `line` | yes | `integer` | mix number (use 0 for first line(mix)) |

## Returns

None.

## Availability

- Since: `2.0.0`
- Radio support: `all`

## Source

`radio/src/lua/api_model.cpp`
