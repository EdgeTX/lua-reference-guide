---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/Ly8RKETivxoHMb7Zzqkb/lua-api-reference/display-lcd/popupwarning
---

# popupWarning(title, event)

Raises a pop-up on screen that shows a warning

@status current Introduced in 2.2.0

## Parameters

* `title` (string) text to display
* `event` (number) the event variable that is passed in from the Run function (key pressed)

## Return value

* `"CANCEL"` user pushed EXIT key

### Notice

Use only from stand-alone and telemetry scripts.
