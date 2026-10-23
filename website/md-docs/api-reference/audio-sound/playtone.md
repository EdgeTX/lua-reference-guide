---
description: Play a tone
---

# playTone(frequency, duration, pause \[, flags \[, freqIncr]])

**Supported targets:** BW, COLOR

**Status:** current Introduced in 2.1.0, changed in 2.10

## Parameters

* `frequency` (number) tone frequency in Hz (from 150 to 15000)
* `duration` (number) length of the tone in milliseconds
* `pause` (number) length of the silence after the tone in milliseconds
* `flags` (number):
  * `0 or not present` play with normal priority.
  * `PLAY_BACKGROUND` play in background (built in vario function uses this context)
  * `PLAY_NOW` play immediately
* `freqIncr` (number) positive number increases the tone pitch (frequency with time), negative number decreases it. The frequency changes every 10 milliseconds, the change is `freqIncr * 10Hz`. The valid range is from -127 to 127.
* `volume` (number): (1..5) override radio settings Beep volume for the duration of file. Omitting the parameter uses radio settings Beep volume

## Return value

none

## Examples

```lua
playTone(2550, 160, 20, 3, -10, 5) -- play tone, use Beep volume 5
playTone(2550, 160, 20, 3, -10, 1) -- play tone, use Beep volume 1
playTone(2550, 160, 20, 3, -10)	   -- play tone, use radio settings Beep volume
```
