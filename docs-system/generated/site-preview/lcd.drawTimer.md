# lcd.drawTimer

`lcd.drawTimer(x, y, value [, flags [, inversColor]])`

Display a value formatted as time at (x,y)

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `x` | yes | `integer` | starting coordinate |
| `y` | yes | `integer` | starting coordinate |
| `value` | yes | `integer` | time in seconds |
| `flags` | no | `integer` | please see [Lcd functions overview](../lcd-functions-less-than-greater-than-luadoc-begin-lcd/lcd_functions-overview.html) |
| `inversColor` | no | `unknown` | overrides the inverse text color for INVERS |

## Returns

None.

## Availability

- Since: `2.0.0`
- Radio support: `bw-lcd`
- Radio support: `color-lcd`

## Source

`radio/src/lua/api_colorlcd.cpp; radio/src/lua/api_stdlcd.cpp`
