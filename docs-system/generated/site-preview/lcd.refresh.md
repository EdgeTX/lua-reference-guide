# lcd.refresh

`lcd.refresh()`

Refresh the LCD screen

## Parameters

None.

## Returns

None.

## Availability

- Since: `2.2.0`
- Radio support: `bw-lcd`
- Radio support: `color-lcd`

## Notes

- From 2.4.0 on color LCDs, this is done automatically when the screen
needs to be refreshed (on events and depending on refresh period).
- This function only works in stand-alone and telemetry scripts.

## Source

`radio/src/lua/api_colorlcd.cpp; radio/src/lua/api_stdlcd.cpp`
