# lcd.RGB\(r, g, b \| rgb\)

Returns a drawing flag with RGB color code

@status current Introduced in 2.2.0

## Parameters

* `r` \(integer\) a number between 0 and 255 that expresses the amount of red in the color
* `g` \(integer\) a number between 0 and 255 that expresses the amount of green in the color
* `b` \(integer\) a number between 0 and 255 that expresses the amount of blue in the color
* `rgb` \(integer\) a number between 0 and 0xFFFFFF that expresses the RGB value \(0xFF000=RED, 0x00FF00=GREEN, 0x0000FF=BLUE\)

## Return value

* `flag` with RGB565 color

### Notice

Only available on radios with color display. Use _either_ lcd.RGB\(r,g,b\) _or_ lcd.RGB\(rgb\).

