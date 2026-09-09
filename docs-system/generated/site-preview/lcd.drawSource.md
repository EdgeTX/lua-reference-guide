# lcd.drawSource

`lcd.drawSource(x, y, source [, flags])`

Displays the name of the corresponding input as defined by the source at (x,y)

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `x` | yes | `integer` | starting coordinate |
| `y` | yes | `integer` | starting coordinate |
| `source` | yes | `integer` | source index |
| `flags` | no | `integer` | please see [Lcd functions overview](../lcd-functions-less-than-greater-than-luadoc-begin-lcd/lcd_functions-overview.html) |

## Returns

None.

## Availability

- Since: `2.0.0`
- Radio support: `bw-lcd`
- Radio support: `color-lcd`

## Source

`radio/src/lua/api_colorlcd.cpp; radio/src/lua/api_stdlcd.cpp`
