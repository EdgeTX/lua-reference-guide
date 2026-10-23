# lcd.drawPixmap

`lcd.drawPixmap(x, y, name)`

Draw a bitmap at (x,y)

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `x` | yes | `integer` | starting coordinates |
| `y` | yes | `integer` | starting coordinates |
| `name` | yes | `string` | full path to the bitmap on SD card (i.e. “/IMAGES/test.bmp”) |

## Returns

None.

## Availability

- Since: `2.0.0`
- Radio support: `bw-lcd`

## Notes

- Maximum image size is [display width / 2] x [display height] pixels.

## Source

`radio/src/lua/api_stdlcd.cpp`
