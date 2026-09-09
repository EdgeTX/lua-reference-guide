# lcd.drawCombobox

`lcd.drawCombobox(x, y, w, list, idx [, flags])`

Draw a combo box

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `x` | yes | `integer` | top left corner position |
| `y` | yes | `integer` | top left corner position |
| `w` | yes | `integer` | width of combo box in pixels |
| `list` | yes | `table` | combo box elements, each element is a string |
| `idx` | yes | `integer` | index of entry to highlight |
| `flags` | no | `integer` | drawing flags, the flags can not be combined: * `BLINK` combo box is expanded  * `INVERS` combo box collapsed, text inversed  * `0 or not present` combo box collapsed, text normal |

## Returns

None.

## Availability

- Since: `2.0.0`
- Radio support: `bw-lcd`

## Notes

- Only available on Taranis

## Source

`radio/src/lua/api_stdlcd.cpp`
