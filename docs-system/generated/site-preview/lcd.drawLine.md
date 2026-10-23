# lcd.drawLine

`lcd.drawLine(x1, y1, x2, y2, pattern, [flags])`

Draw a straight line on LCD

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `x1` | yes | `integer` | starting coordinate |
| `y1` | yes | `integer` | starting coordinate |
| `x2` | yes | `integer` | end coordinate |
| `y2` | yes | `integer` | end coordinate |
| `pattern` | yes | `unknown` | SOLID or DOTTED |
| `flags` | no | `integer` | lcdflags |

## Returns

None.

## Availability

- Since: `2.0.0`
- Radio support: `bw-lcd`
- Radio support: `color-lcd`

## Notes

- If the start or the end of the line is outside the LCD dimensions, then the
whole line will not be drawn (starting from OpenTX 2.1.5)

## Source

`radio/src/lua/api_colorlcd.cpp; radio/src/lua/api_stdlcd.cpp`
