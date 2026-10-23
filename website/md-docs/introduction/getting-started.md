# Getting Started

## Downloading EdgeTX Companion

EdgeTX Companion 2.5 is [available for download here](https://github.com/EdgeTX/edgetx/releases/tag/v2.5.0) (pick the version for your operating system from Assets heading at the bottom of the page).&#x20;

## Updating firmware with Lua option selected

If you intend to use mixer scripts, when updating the firmware on your transmitter you need to make sure the `lua` option is checked in the settings for your radio profile (Main menu -> Settings ->Settings...) as shown below. This is not required if you only intend to run telemetry, one-time and function scripts, support for those is included by default.

Also note that the SD Structure path should contain a valid path to a copy of your transmitter's SD card contents, although that's not specific to Lua.

![Edit Settings dialog from EdgeTX Companion](https://github.com/opentx/opentx-2-3-lua-reference-guide/tree/0d355d19f1961b689994cf78b84005864d33f9b5/companion-settings.png)
