# lcd.RGB

`lcd.RGB(r, g, b | rgb)`

Returns a drawing flag with RGB color code

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `r` | yes | `integer` | a number between 0 and 255 that expresses the amount of red in the color |
| `g` | yes | `integer` | a number between 0 and 255 that expresses the amount of green in the color |
| `b` | yes | `integer` | a number between 0 and 255 that expresses the amount of blue in the color |
| `rgb` | yes | `integer` | a number between 0 and 0xFFFFFF that expresses the RGB value (0xFF000=RED, 0x00FF00=GREEN, 0x0000FF=BLUE) |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `flag` | `integer` | with RGB565 color |

## Availability

- Since: `2.2.0`
- Radio support: `color-lcd`

## Notes

- Only available on radios with color display. Use *either* lcd.RGB(r,g,b) *or* lcd.RGB(rgb)

## Source

`radio/src/lua/api_colorlcd.cpp`
