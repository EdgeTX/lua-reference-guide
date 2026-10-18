# defaultStick

`defaultStick(channel)`

Get stick that is assigned to a channel. See Default Channel Order in General Settings.

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `channel` | yes | `integer` | channel number (0 means CH1) |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `-` | `integer` | Stick assigned to this channel (from 0 to 3) |

## Availability

- Since: `2.0.0`
- Radio support: `all`

## Source

`radio/src/lua/api_general.cpp`
