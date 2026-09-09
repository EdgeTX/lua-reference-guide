# lcd.drawSwitch

`lcd.drawSwitch(x, y, switch, flags)`

Draw a text representation of switch at (x,y)

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `x` | yes | `integer` | starting coordinate |
| `y` | yes | `integer` | starting coordinate |
| `switch` | yes | `integer` | number of switch to display, negative number displays negated switch |
| `flags` | yes | `integer` | please see [Lcd functions overview](../lcd-functions-less-than-greater-than-luadoc-begin-lcd/lcd_functions-overview.html), only SMLSIZE, BLINK and INVERS. |

## Returns

None.

## Availability

- Since: `2.0.0`
- Radio support: `bw-lcd`
- Radio support: `color-lcd`

## Source

`radio/src/lua/api_colorlcd.cpp; radio/src/lua/api_stdlcd.cpp`
