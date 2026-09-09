# lcd.drawLineWithClipping

`lcd.drawLineWithClipping(x1, y1, x2, y2, xmin, xmax, ymin, ymax, pattern [, flags])`

Draw a line only inside a rectangle

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `x1` | yes | `integer` | coordinates of the start and end of the unclipped line |
| `y1` | yes | `integer` | coordinates of the start and end of the unclipped line |
| `x2` | yes | `integer` | coordinates of the start and end of the unclipped line |
| `y2` | yes | `integer` | coordinates of the start and end of the unclipped line |
| `xmin` | yes | `integer` | the limits of the rectangle inside which the line is drawn |
| `xmax` | yes | `integer` | the limits of the rectangle inside which the line is drawn |
| `ymin` | yes | `integer` | the limits of the rectangle inside which the line is drawn |
| `ymax` | yes | `integer` | the limits of the rectangle inside which the line is drawn |
| `pattern` | yes | `FORCE,-ERASE,-DOTTED` | please see [Lcd functions overview](../lcd-functions-less-than-greater-than-luadoc-begin-lcd/lcd_functions-overview.html) |
| `flags` | no | `integer` | please see [Lcd functions overview](../lcd-functions-less-than-greater-than-luadoc-begin-lcd/lcd_functions-overview.html) |

## Returns

None.

## Availability

- Since: `2.4.0`
- Radio support: `color-lcd`

## Notes

- Only available on radios with color display

## Source

`radio/src/lua/api_colorlcd.cpp`
