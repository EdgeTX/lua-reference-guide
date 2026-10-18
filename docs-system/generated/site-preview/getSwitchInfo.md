# getSwitchInfo

`getSwitchInfo(sourceIndex)`



## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `sourceIndex` | yes | `integer` | identifying a value source as returned by `getSourceIndex(sourceName)` or the `id` field in the table returned by `getFieldInfo`. |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `-` | `table` | information about requested field, table elements: * `type`   (number) field identifier 0 = SWITCH_NONE 1 = SWITCH_TOGGLE 2 = SWITCH_2POS 3 = SWITCH_3POS |

## Availability

- Since: `2.12`
- Radio support: `all`

## Source

`radio/src/lua/api_general.cpp`
