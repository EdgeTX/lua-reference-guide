# popupConfirmation\(title, message, event\)

Raises a pop-up on screen that asks for confirmation

@status current Introduced in 2.2.0, changed from \(title, event\) to \(title, message, event\) in 2.3.8

## Parameters

* `title` \(string\) title to display
* `message` \(string\) text to display
* `event` \(number\) the event variable that is passed in from the Run function \(key pressed\)

## Return value

* `"CANCEL"` user pushed EXIT key

### Notice

Use only from stand-alone and telemetry scripts.

