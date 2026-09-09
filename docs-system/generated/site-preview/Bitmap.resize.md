# Bitmap.resize

`Bitmap.resize(bitmap, width, height)`

Return a resized bitmap object

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `bitmap` | yes | `pointer` | point to a bitmap previously opened with Bitmap.open() |
| `width` | yes | `integer` | the new bitmap width |
| `height` | yes | `integer` | the new bitmap height |

## Returns

None.

## Availability

- Since: `2.8.0`
- Radio support: `color-lcd`

## Notes

- Only available on radios with color display

## Source

`radio/src/lua/api_colorlcd.cpp`
