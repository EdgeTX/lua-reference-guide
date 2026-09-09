# lcd.clear

`lcd.clear([color])`

Clear the LCD screen

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `color` | no | `unknown` |  |

## Returns

None.

## Availability

- Since: `2.0.0`
- Radio support: `bw-lcd`
- Radio support: `color-lcd`

## Notes

- This function only works in stand-alone and telemetry scripts.

## Source

`radio/src/lua/api_colorlcd.cpp; radio/src/lua/api_stdlcd.cpp`
