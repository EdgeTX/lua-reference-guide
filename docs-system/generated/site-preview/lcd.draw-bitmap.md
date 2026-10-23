# lcd.drawBitmap

`lcd.drawBitmap(bitmap, x, y [, scale])`

Display a previously opened bitmap at coordinates and optionally scale it.

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `bitmap` | yes | `bitmapPointer` | Pointer returned by Bitmap.open(). |
| `x` | yes | `integer` | Top coordinate. |
| `y` | yes | `integer` | Left coordinate. |
| `scale` | no | `integer` | Scale percent where 100 keeps original size. |

## Returns

None.

## Availability

- Since: `2.3.0`
- Radio support: `color-lcd`

## Notes

- Only available on radios with color display.

## Source

`radio/src/lua/api_colorlcd.cpp`

## Enrichment

The sections below are authored outside the firmware source so examples, compatibility notes, and learning material can evolve without bloating C++ API comments.

## Extended Description

`lcd.drawBitmap` is a good example of the split between generated API truth and richer authored guidance. The syntax, parameter list, and availability belong in upstream source annotations. Practical usage notes and examples can stay here in an overlay file.

## Examples

```lua
local bmp = Bitmap.open("/IMAGES/logo.png")
if bmp then
  lcd.drawBitmap(bmp, 10, 12, 100)
end
```

## Related Topics

- `Bitmap.open`
- `Bitmap.getSize`
