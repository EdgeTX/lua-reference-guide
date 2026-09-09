# lcd.drawBitmapPatternPie

`lcd.drawBitmapPatternPie(bitmap, x, y, startAngle, endAngle [, flags])`

Displays a bitmap pattern pie at (x,y)

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `bitmap` | yes | `pointer` | point to a bitmap previously opened with Bitmap.open() |
| `x` | yes | `integer` | starting coordinates |
| `y` | yes | `integer` | starting coordinates |
| `startAngle` | yes | `unknown` | Start angle |
| `endAngle` | yes | `unknown` | End angle |
| `flags` | no | `integer` | please see [Lcd functions overview](../lcd-functions-less-than-greater-than-luadoc-begin-lcd/lcd_functions-overview.html) |

## Returns

None.

## Availability

- Since: `2.8.0`
- Radio support: `color-lcd`

## Notes

- Only available on radios with color display

## Source

`radio/src/lua/api_colorlcd.cpp`
