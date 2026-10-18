# Bitmap.toMask

`Bitmap.toMask(bitmap)`

Return a 8bit bitmap mask that can be used with lcd.drawBitmapPattern()

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `bitmap` | yes | `pointer` | point to a bitmap previously opened with Bitmap.open() |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `a` | `unknown` | bitmap mask |

## Availability

- Since: `2.8.0`
- Radio support: `color-lcd`

## Notes

- Only available on radios with color display

## Source

`radio/src/lua/api_colorlcd.cpp`
