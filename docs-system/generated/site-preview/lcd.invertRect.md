# lcd.invertRect

`lcd.invertRect(x, y, w, h [, flags])`

Invert a rectangle zone from top left corner (x,y) of specified width and height

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `x` | yes | `integer` | top left corner position |
| `y` | yes | `integer` | top left corner position |
| `w` | yes | `integer` | width in pixels |
| `h` | yes | `integer` | height in pixels |
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
