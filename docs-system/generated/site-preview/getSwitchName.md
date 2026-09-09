# getSwitchName

`getSwitchName(switchIndex)`



## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `switchIndex` | yes | `integer` | identifying a switch as returned by `getSwitchIndex(positionName)` or fields in the table returned by `model.getLogicalSwitch(switch)` identifying switches. |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `value` | `string` | naming the switch position as it is shown on radio menus where a switch can be chosen. |

## Availability

- Since: `2.6`
- Radio support: `all`

## Source

`radio/src/lua/api_general.cpp`
