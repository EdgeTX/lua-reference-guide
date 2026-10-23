# model.insertMix

`model.insertMix(channel, line, value)`

Insert a mixer line into Channel

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `channel` | yes | `integer` | channel number (use 0 for CH1) |
| `line` | yes | `integer` | mix number (use 0 for first line(mix)) |
| `value` | yes | `table` | see model.getMix() for table format |

## Returns

None.

## Availability

- Since: `2.0.0`
- Radio support: `all`

## Source

`radio/src/lua/api_model.cpp`
