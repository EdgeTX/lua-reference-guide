# Quick Start

## Downloading EdgeTX Companion

EdgeTX Companion 2.10 is [available for download here](https://github.com/EdgeTX/edgetx/releases/tag/v2.10.0) (pick the appropriate download for your operating system from Assets heading at the bottom of the page - the filename will have `cpn` in the name).

## Enabling support for Mixer Scripts

If you intend to use mixer scripts, when compiling the firmware for your transmitter you need to make sure the `LUA_MIXER` option is set. This is not required if you only intend to run any of the other types of Lua script (i.e. telemetry, one-time, function scripts, widgets) as support for those is included by default.
