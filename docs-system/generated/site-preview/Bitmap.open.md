# Bitmap.open

`Bitmap.open(name)`

Loads a bitmap in memory, for later use with lcd.drawBitmap(). Bitmaps should be loaded only
once, returned object should be stored and used for drawing. If loading fails for whatever
reason the resulting bitmap object will have width and height set to zero.

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `name` | yes | `string` | full path to the bitmap on SD card (i.e. “/IMAGES/test.bmp”) |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `bitmap` | `object` | a bitmap object that can be used with other bitmap functions |

## Availability

- Since: `2.2.0`
- Radio support: `color-lcd`

## Notes

- Bitmap loading can fail if:
 * File is not found or contains invalid image
 * System is low on memory
 * Combined memory usage of all Lua script bitmaps exceeds certain value
- Only available on radios with color display

## Source

`radio/src/lua/api_colorlcd.cpp`
