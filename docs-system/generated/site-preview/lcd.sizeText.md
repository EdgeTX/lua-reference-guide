# lcd.sizeText

`lcd.sizeText(text [, flags])`

Get the width and height of a text string drawn with flags

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `text` | yes | `string` |  |
| `flags` | no | `integer` | please see [Lcd functions overview](../lcd-functions-less-than-greater-than-luadoc-begin-lcd/lcd_functions-overview.html) |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `w,h` | `integer` | width and height of the text |

## Availability

- Since: `2.5.0`
- Radio support: `color-lcd`

## Notes

- Only available on radios with color display

## Source

`radio/src/lua/api_colorlcd.cpp`
