# lcd.drawPie

`lcd.drawPie(x, y, r, start, end [, flags])`

Draw a pie slice

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `x` | yes | `integer` | coordinates of the center |
| `y` | yes | `integer` | coordinates of the center |
| `r` | yes | `integer` | radius |
| `start` | yes | `integer` | start and end of the pie slice |
| `end` | yes | `integer` | start and end of the pie slice |
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
