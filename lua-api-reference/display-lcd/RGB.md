# lcd.RGB(r, g, b | rgb)

Returns a 5/6/5 rgb color code, that can be used with lcd.setColor

@status current Introduced in 2.2.0

### Parameters

* `r` (required) \[integer] number between 0x00 and 0xff that expresses te amount of red in the color
* `g` (required) \[integer] number between 0x00 and 0xff that expresses te amount of green in the color
* `b` (required) \[integer]  number between 0x00 and 0xff that expresses te amount of blue in the color

or

* `rgb` (required) \[integer]  number between 0 and 0xFFFFFF that expresses the RGB value (0xFF0000=RED, 0x00FF00=GREEN, 0x0000FF=BLUE)

### Return value

* `color_flag`.   See [Drawing Flags](../../lua-api-programming/drawing-flags-and-colors.md)

### Avaiable on

* [ ] B\&W LCD radios
* [ ] Grayscale LCD radios
* [x] Color LCD radios
