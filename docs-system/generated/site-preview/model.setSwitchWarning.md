# model.setSwitchWarning

`model.setSwitchWarning(switch, state)`

Set warning state for a switch

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `switch` | yes | `integer` | switch number (use 0 for SA) @param switch (string) switch name |
| `state` | yes | `integer` | state 0 = no warning 1 = switch up 2 = switch middle 3 = switch down |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `-` | `nil` | when switch is a toggle or does not exist |

## Availability

- Since: `3.0.0`
- Radio support: `all`

## Source

`radio/src/lua/api_model.cpp`
