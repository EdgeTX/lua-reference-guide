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
