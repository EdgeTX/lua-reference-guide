# model.getMixesCount

`model.getMixesCount(channel)`

Get the number of Mixer lines that the specified Channel has

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `channel` | yes | `integer` | channel number (use 0 for CH1) |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `-` | `integer` | number of mixes for requested channel |

## Availability

- Since: `2.0.0`
- Radio support: `all`

## Source

`radio/src/lua/api_model.cpp`
