# lcd.drawTextLines

`lcd.drawTextLines(x, y, w, h, text [, flags])`

Draw text inside rectangle (x,y,w,h) with line breaks

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `x` | yes | `integer` | starting coordinate |
| `y` | yes | `integer` | starting coordinate |
| `w` | yes | `integer` | width and height of bounding rectangle |
| `h` | yes | `integer` | width and height of bounding rectangle |
| `text` | yes | `string` | text to display |
| `flags` | no | `integer` | please see [Lcd functions overview](../lcd-functions-less-than-greater-than-luadoc-begin-lcd/lcd_functions-overview.html) for drawing flags and colors, and [Appendix](../../part_vii_-_appendix/fonts.md) for available characters in each font set. RIGHT, CENTER and VCENTER are not implemented. |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `x,y` | `integer` | point where text drawing ended |

## Availability

- Since: `2.5.0`
- Radio support: `color-lcd`

## Notes

- Only available on radios with color display

## Source

`radio/src/lua/api_colorlcd.cpp`
