---
description: Play a time value (text to speech)
---

# playDuration(duration \[, hourFormat])

**Supported Targets:** BW, COLOR

**Status:** current Introduced in 2.1.0, changed in 2.10

## Parameters

* `duration` (number) number of seconds to play. Only integral part is used.
* `hourFormat` (number):
  * `0 or not present` play format: minutes and seconds.
  * `!= 0` play format: hours, minutes and seconds.

## Return value

none

## Examples

```lua
playDuration(101, 0, 5) -- play duration 101s, seconds format, use Wav volume 5
playDuration(101, 0, 1) -- play duration 101s, seconds format, use Wav volume 1
playDuration(101, 1)    -- play duration 101s, hour format, use radio settings Wav volume
```
