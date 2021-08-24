# lcd.drawText\(x, y, text \[, flags\]\)

Draw a text beginning at \(x,y\)

@status current Introduced in 2.0.0, `SHADOWED` introduced in 2.2.1

## Parameters

* `x,y` \(positive numbers\) starting coordinate
* `text` \(string\) text to display
* `flags` \(unsigned number\) drawing flags. All values can be combined together using the + character. ie BLINK + DBLSIZE. See the [Appendix](https://github.com/EdgeTX/lua-reference-guide/tree/fe42fe461fcccd828fba5d218da01336e4f7b0cd/part_iii_-_opentx_lua_api_reference/appendix/fonts.md) for available characters in each font set.
  * `0 or not specified` normal font
  * `XXLSIZE` jumbo sized font
  * `DBLSIZE` double size font
  * `MIDSIZE` mid sized font
  * `SMLSIZE` small font
  * `INVERS` inverted display
  * `BLINK` blinking text
  * `SHADOWED` Horus only, apply a shadow effect

## Return value

none

