---
description: Play a file from the SD card
---

# playFile(name)

**Supported targets:** BW, COLOR

**Status:** current Introduced in 2.0.0, changed in 2.1.0, changed in 2.10\\

## Parameters

*   `filename` (string) full path to wav file (i.e. “/SOUNDS/en/system/tada.wav”)

    Introduced in 2.1.0: If you use a relative path, the current language is appended

    to the path (example: for English language: `/SOUNDS/en` is appended)
* `volume` (number): (1..5) override radio settings Wav volume for the duration of file. Omitting the parameter uses radio settings Wav volume

## Return value

none

## Examples

```lua
playFile("armed.wav", 5) -- play file armed.wav, use Wav volume 2
playFile("armed.wav", 1) -- play file armed.wav, use Wav volume 1
playFile("armed.wav")	 -- play file armed.wav, use radio settings Wav volume
```
