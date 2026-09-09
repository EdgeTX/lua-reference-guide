# lcd.setColor

`lcd.setColor(colorIndex, color)`

Change an indexed color (theme colors and CUSTOM_COLOR). Please see [Lcd functions overview](../lcd-functions-less-than-greater-than-luadoc-begin-lcd/lcd_functions-overview.html#color-constants)

## Parameters

None.

## Returns

None.

## Availability

- Since: `2.2.0`
- Radio support: `color-lcd`

## Notes

- Please notice that changing theme colors affects not only other Lua widgets, but the entire radio interface.
- Only available on radios with color display

## Source

`radio/src/lua/api_colorlcd.cpp`
