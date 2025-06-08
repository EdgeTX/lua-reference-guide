---
description: Constants defined for use in LVGL layouts.
---

# Constants

<table><thead><tr><th width="206">Name</th><th>Description</th></tr></thead><tbody><tr><td>lvgl.FLOW_ROW</td><td>Sets flex layout flow.</td></tr><tr><td>lvgl.FLOW_COLUMN</td><td>Set flex layout flow.</td></tr><tr><td>lvgl.PAD_TINY</td><td>2 pixel padding.</td></tr><tr><td>lvgl.PAD_SMALL</td><td>4 pixel padding.</td></tr><tr><td>lvgl.PAD_MEDIUM</td><td>6 pixel padding.</td></tr><tr><td>lvgl.PAD_LARGE</td><td>8 pixel padding.</td></tr><tr><td>lvgl.PAD_OUTLINE</td><td>Padding required around controls for focus outline.</td></tr></tbody></table>

Constants for the 'filter' property of the lvgl.source control. Can be used to limit which sources the user can select.

<table><thead><tr><th width="206">Name</th><th>Description</th></tr></thead><tbody><tr><td>lvgl.SRC_ALL</td><td>Allow all source types, enable the 'Clear' button and the 'Invert' button.</td></tr><tr><td>lvgl.SRC_INPUT</td><td>Inputs</td></tr><tr><td>lvgl.SRC_STICK</td><td>Analog sticks</td></tr><tr><td>lvgl.SRC_POT</td><td>Pots and sliders</td></tr><tr><td>lvgl.SRC_SWITCH</td><td>Switches</td></tr><tr><td>lvgl.SRC_CHANNEL</td><td>Outputs</td></tr><tr><td>lvgl.SRC_TRIM</td><td>Trims</td></tr><tr><td>lvgl.SRC_LOGICAL_SWITCH</td><td>Logical switches</td></tr><tr><td>lvgl.SRC_GVAR</td><td>Global variables</td></tr><tr><td>lvgl.SRC_LUA</td><td>Custom Lua mix script outputs</td></tr><tr><td>lvgl.SRC_OTHER</td><td>MIN, MAX, tx battery, timers etc.</td></tr><tr><td>lvgl.SRC_HELI</td><td>Heli channels</td></tr><tr><td>lvgl.SRC_TRAINER</td><td>Trainer channels</td></tr><tr><td>lvgl.SRC_TELEM</td><td>Telemetry sensors</td></tr><tr><td>lvgl.SRC_CLEAR</td><td>Special value to control the 'Clear' button in the source chooser.</td></tr><tr><td>lvgl.SRC_INVERT</td><td>Special value to control the 'Invert' button in the source chooser.</td></tr></tbody></table>

Constants for the 'filter' property of the lvgl.witch control. Can be used to limit which sources the user can select.

<table><thead><tr><th width="206">Name</th><th>Description</th></tr></thead><tbody><tr><td>lvgl.SW_ALL</td><td>Allow all switch types, enable the 'Clear' button.</td></tr><tr><td>lvgl.SW_SWITCH</td><td>Switches</td></tr><tr><td>lvgl.SW_TRIM</td><td>Trims</td></tr><tr><td>lvgl.SW_LOGICAL_SWITCH</td><td>Logical switches</td></tr><tr><td>lvgl.SW_FLIGHT_MODE</td><td>Flight modes</td></tr><tr><td>lvgl.SW_TELEM</td><td>Telemetry sensors</td></tr><tr><td>lvgl.SW_OTHER</td><td>ON, ONE, trainer connected, radio activity, etc</td></tr><tr><td>lvgl.SW_CLEAR</td><td>Special value to control the 'Clear' button in the switch chooser.</td></tr></tbody></table>

Constants to control scrolling of containers such as box and rectangle

<table><thead><tr><th width="206">Name</th><th>Description</th></tr></thead><tbody><tr><td>lvgl.SCROLL_OFF</td><td>No scrolling allowed. Objects outside the containers boundary will be clipped</td></tr><tr><td>lvgl.SCROLL_HOR</td><td>Horizontal scrolling only</td></tr><tr><td>lvgl.SCROLL_VER</td><td>Vertical scrolling only</td></tr><tr><td>lvgl.SCROLL_ALL</td><td>Both horizontal and vertical scrolling allowed</td></tr></tbody></table>
