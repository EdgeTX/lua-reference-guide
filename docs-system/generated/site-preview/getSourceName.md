# getSourceName

`getSourceName(sourceIndex)`



## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `sourceIndex` | yes | `integer` | identifying a value source as returned by `getSourceIndex(sourceName)` or the `id` field in the table returned by `getFieldInfo`. |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `sourceName` | `string` | naming the value source as it is shown on radio menus where a source can be chosen. |

## Availability

- Since: `2.6`
- Radio support: `all`

## Notes

- the source names shown on the screen are not the same as the names used by `getFieldInfo` and `getValue`. But the indices are the same, so `getValue(index)` will work with the indices used here.

## Source

`radio/src/lua/api_general.cpp`
