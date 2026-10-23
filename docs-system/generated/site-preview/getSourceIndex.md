# getSourceIndex

`getSourceIndex(sourceName)`



## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `sourceName` | yes | `string` | naming a value source as it is shown on radio menus where you can select it. Notice that many names have special characters in them. |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `sourceIndex` | `integer` | . The source index, which can be used as input for `getSourceName(sourceIndex)`, `getValue(sourceIndex)`, and `getFieldInfo(sourceIndex)`. |

## Availability

- Since: `2.6`
- Radio support: `all`

## Notes

- the source names shown on the screen are not the same as the names used by `getFieldInfo` and `getValue`. But the indices are the same, so `getValue(index)` will work with the indices obtained here.
This function is rather time consuming, and should not be used repeatedly in a script, if it can be avoided.

## Source

`radio/src/lua/api_general.cpp`
