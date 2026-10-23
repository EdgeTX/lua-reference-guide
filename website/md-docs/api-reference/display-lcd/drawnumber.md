# lcd.drawNumber(x, y, value \[, flags])

Display a number at (x,y)

@status current Introduced in 2.0.0, `SHADOWED` introduced in 2.2.1

### Parameters

* `x,y` (positive numbers) starting coordinate
* `value` (number) value to display
* `flags` (unsigned number) drawing [flags](../constants/flags-and-pattern-constants.md):
  * `0 or not specified` display with no decimal (like abs())
  * `PREC1` display with one decimal place (number 386 is displayed as 38.6)
  * `PREC2` display with tow decimal places (number 386 is displayed as 3.86)
  * other general LCD [flags](../constants/flags-and-pattern-constants.md) also apply\\

### Return value

none
