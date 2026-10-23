# lcd.getColor

`lcd.getColor(flags)`

Get the color value from flags

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `flags` | yes | `integer` | please see [Lcd functions overview](../lcd-functions-less-than-greater-than-luadoc-begin-lcd/lcd_functions-overview.html) |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `color` | `flag` | only the RGB565 color value of the input |

## Availability

- Since: `2.3.11`
- Radio support: `color-lcd`

## Notes

- Only available on radios with color display

## Source

`radio/src/lua/api_colorlcd.cpp`
