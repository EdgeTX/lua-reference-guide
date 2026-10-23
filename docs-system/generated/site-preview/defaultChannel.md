# defaultChannel

`defaultChannel(stick)`

Get channel assigned to stick. See Default Channel Order in General Settings

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `stick` | yes | `integer` | stick number (from 0 to 3) |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `-` | `integer` | channel assigned to this stick (from 0 to 3) |
| `-` | `nil` | stick not found |

## Availability

- Since: `2.0.0`
- Radio support: `all`

## Source

`radio/src/lua/api_general.cpp`
