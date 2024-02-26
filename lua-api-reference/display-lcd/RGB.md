# lcd.RGB( r, g, b | rgb )

### Description

Returns a 5/6/5 rgb color code, that can be used with lcd.setColor

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

### Examples

`local darkred = lcd.RGB(20,0,0)  -- create color_flag for color`\
`lcd.drawText(0,0,"Very dark red text", darkred)`\
\
`local mygrey = lcd.RGB(0xAEAEAE)  -- create color_flag for color`\
`lcd.drawText(0,20,"My grey color", mygrey)`\
&#x20;
