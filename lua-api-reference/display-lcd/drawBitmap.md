# lcd.drawBitmap(bitmap, x, y \[, scale])

Displays a bitmap at (x,y)

@status current Introduced in 2.2.0

### Parameters

* `bitmap` (pointer) point to a bitmap previously opened with Bitmap.open()
* `x,y` (positive numbers) starting coordinates
* `scale` (positive numbers) scale in %, 50 divides size by two, 100 is unchanged, 200 doubles size. Omitting scale draws image in 1:1 scale and is faster than specifying 100 for scale.

### Return value

none

#### Notice

Only available on Horus



### Description

Displays a bitmap at (x,y)

### Parameters

* `r` (required) \[integer] number between 0x00 and 0xff that expresses te amount of red in the color
* `g` (required) \[integer] number between 0x00 and 0xff that expresses te amount of green in the color
* `b` (required) \[integer]  number between 0x00 and 0xff that expresses te amount of blue in the color

or

* `rgb` (required) \[integer]  number between 0 and 0xFFFFFF that expresses the RGB value (0xFF0000=RED, 0x00FF00=GREEN, 0x0000FF=BLUE)

### Returns

* `color_flag`.   See [Drawing Flags](../../lua-api-programming/drawing-flags-and-colors.md)

### Notes

### Available on

* [ ] [B\&W LCD radios](../../overview/radios/#radios-with-b-and-w-lcd-screen)
* [ ] [Grayscale LCD radios](../../overview/radios/#radios-with-grayscale-lcd-screen)
* [x] [Color LCD radios](../../overview/radios/#radios-with-color-lcd-screen)

### API status

<table><thead><tr><th width="166">EdgeTX version</th><th width="573">Action</th></tr></thead><tbody><tr><td>2.3.0</td><td>Introduced</td></tr></tbody></table>

\-
