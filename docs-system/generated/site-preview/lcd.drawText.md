# lcd.drawText

`lcd.drawText(x, y, text [, flags [, inversColor]])`

Draw a text beginning at (x,y)

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `x` | yes | `integer` | starting coordinate |
| `y` | yes | `integer` | starting coordinate |
| `text` | yes | `string` | text to display |
| `flags` | no | `integer` | please see [Lcd functions overview](../lcd-functions-less-than-greater-than-luadoc-begin-lcd/lcd_functions-overview.html) for drawing flags and colors, and [Appendix](../../part_vii_-_appendix/fonts.md) for available characters in each font set. |
| `inversColor` | no | `unknown` | overrides the inverse text color for INVERS |

## Returns

None.

## Availability

- Since: `2.0.0`
- Radio support: `bw-lcd`
- Radio support: `color-lcd`

## Source

`radio/src/lua/api_colorlcd.cpp; radio/src/lua/api_stdlcd.cpp`
