# Bitmap.getSize

`Bitmap.getSize(name)`

Return width, height of a bitmap object

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `name` | yes | `pointer` | point to a bitmap previously opened with Bitmap.open() |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `width_in_pixels` | `integer` | width in pixels |
| `height_in_pixels` | `integer` | height in pixels |

## Availability

- Since: `2.2.0`
- Radio support: `color-lcd`

## Notes

- Only available on radios with color display

## Source

`radio/src/lua/api_colorlcd.cpp`
