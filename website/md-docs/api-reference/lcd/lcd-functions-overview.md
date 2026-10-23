# Lcd Functions Overview

### Description

Lcd functions allow scripts to interact with the transmitter display. This access is limited to the `run` function of One-Time and Telemetry scripts, and the `refresh `function of Widget scripts on radios with color display.

### Notes:

The run function is periodically called when the screen is visible. In OpenTX 2.0 each invocation starts with a blank screen (unless lcd.lock() is used). Under OpenTX 2.1 screen state is always persisted across calls to the run function. **Many scripts originally written for OpenTX 2.0 require a call to lcd.clear() at the beginning of their run function in order to display properly under 2.1 and 2.2.**

For Widget scripts, `lcd.clear()` is not needed, as each invocation starts with a blank screen showing the theme background. But it can be used to overwrite the theme background with another color by calling `lcd.clear(color)`.

Please see above for a description of the constants for [flags and patterns](../constants/flags-and-pattern-constants.md), [colors](../constants/color-constants.md), and [screen size](../constants/screen-constants.md) that can be used with lcd drawing functions.
