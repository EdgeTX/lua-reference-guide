---
description: Play a numerical value (text to speech)
---

# playNumber(value, unit \[, attributes])

**Supported Targets:** BW, COLOR

**Status:** current Introduced in 2.0.0, changed in 2.10

## Parameters

* `value` (number) number to play. Value is interpreted as integer.
* `unit` (number) unit identifier \[Full list]\((../appendix/units.html))
* `attributes` (unsigned number) possible values:
  * `0 or not present` plays integral part of the number (for a number 123 it plays 123)
  * `PREC1` plays a number with one decimal place (for a number 123 it plays 12.3)
  * `PREC2` plays a number with two decimal places (for a number 123 it plays 1.23)
* `volume` (number): (1..5) override radio settings Wav volume for the duration of file. Omitting the parameter uses radio settings Wav volume

## Return value

none

## Examples

```lua
playNumber(123, 3, 0, 5) -- play number 123, unit mAh, use Wav volume 5
playNumber(123, 3, 0, 1) -- play number 123, unit mAh, use Wav volume 1
playNumber(123, 3, 0)    -- play number 123, unit mAh, use radio settings Wav volume
```
