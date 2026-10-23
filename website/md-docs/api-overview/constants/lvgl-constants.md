---
description: LVGL-specific constants used for layout, pickers, scrolling, and object construction.
---

# LVGL Constants

These constants are specific to the LVGL UI layer used on color-screen radios. They are most useful when building layouts, constraining picker controls, or creating objects dynamically.

For the broader LVGL guide, see [Using LVGL Library](../../programming/core-concepts/lvgl-for-lua.md). For the constructor pages, see [Display LVGL](../../api-reference/display-lvgl/index.md).

## Layout and Padding

| Name | Description |
| --- | --- |
| `lvgl.FLOW_ROW` | Flex layout flow in rows. |
| `lvgl.FLOW_COLUMN` | Flex layout flow in columns. |
| `lvgl.PAD_TINY` | `2` pixel padding. |
| `lvgl.PAD_SMALL` | `4` pixel padding. |
| `lvgl.PAD_MEDIUM` | `6` pixel padding. |
| `lvgl.PAD_LARGE` | `8` pixel padding. |
| `lvgl.PAD_OUTLINE` | Padding needed around controls for the focus outline. |
| `lvgl.PAD_BORDER` | Default border padding around controls. |

## Source Picker Filters

These constants limit what can be selected by `lvgl.source`.

| Name | Description |
| --- | --- |
| `lvgl.SRC_ALL` | Allow all source types and enable `Clear` and `Invert`. |
| `lvgl.SRC_INPUT` | Inputs. |
| `lvgl.SRC_STICK` | Analog sticks. |
| `lvgl.SRC_POT` | Pots and sliders. |
| `lvgl.SRC_SWITCH` | Switches. |
| `lvgl.SRC_CHANNEL` | Outputs. |
| `lvgl.SRC_TRIM` | Trims. |
| `lvgl.SRC_LOGICAL_SWITCH` | Logical switches. |
| `lvgl.SRC_GVAR` | Global variables. |
| `lvgl.SRC_LUA` | Lua mix-script outputs. |
| `lvgl.SRC_OTHER` | MIN, MAX, timers, battery, and other sources. |
| `lvgl.SRC_HELI` | Heli channels. |
| `lvgl.SRC_TRAINER` | Trainer channels. |
| `lvgl.SRC_TELEM` | Telemetry sensors. |
| `lvgl.SRC_CLEAR` | Controls the `Clear` button in the source chooser. |
| `lvgl.SRC_INVERT` | Controls the `Invert` button in the source chooser. |

## Switch Picker Filters

These constants limit what can be selected by `lvgl.switch`.

| Name | Description |
| --- | --- |
| `lvgl.SW_ALL` | Allow all switch types and enable `Clear`. |
| `lvgl.SW_SWITCH` | Physical switches. |
| `lvgl.SW_TRIM` | Trims. |
| `lvgl.SW_LOGICAL_SWITCH` | Logical switches. |
| `lvgl.SW_FLIGHT_MODE` | Flight modes. |
| `lvgl.SW_TELEM` | Telemetry-driven switches. |
| `lvgl.SW_OTHER` | `ON`, `ONE`, trainer connected, radio activity, and similar sources. |
| `lvgl.SW_CLEAR` | Controls the `Clear` button in the switch chooser. |

## Scrolling

| Name | Description |
| --- | --- |
| `lvgl.SCROLL_OFF` | Disable scrolling; overflow is clipped. |
| `lvgl.SCROLL_HOR` | Horizontal scrolling only. |
| `lvgl.SCROLL_VER` | Vertical scrolling only. |
| `lvgl.SCROLL_ALL` | Horizontal and vertical scrolling. |

## Screen and Page Layout

These constants help scripts adapt to different screen sizes. The page-related values were added in EdgeTX `2.11.4`.

| Name | Description |
| --- | --- |
| `lvgl.PAGE_BODY_HEIGHT` | Height of the body section inside an LVGL page. |
| `lvgl.UI_ELEMENT_HEIGHT` | Default height for common controls such as buttons, toggles, and sliders. |
| `lvgl.LCD_SCALE` | Scale factor relative to a `480x272` display. |
| `lvgl.PERCENT_SIZE` | Base value for percentage-based sizes and positions, used as `lvgl.PERCENT_SIZE + N`. |

## Object Type Constants

These constants can be used with `lvgl.build` instead of string type names. They were added in EdgeTX `2.11.4`.

| Name | Equivalent to |
| --- | --- |
| `lvgl.LABEL` | `"label"` |
| `lvgl.RECTANGLE` | `"rectangle"` |
| `lvgl.CIRCLE` | `"circle"` |
| `lvgl.ARC` | `"arc"` |
| `lvgl.HLINE` | `"hline"` |
| `lvgl.VLINE` | `"vline"` |
| `lvgl.LINE` | `"line"` |
| `lvgl.TRIANGLE` | `"triangle"` |
| `lvgl.IMAGE` | `"image"` |
| `lvgl.QRCODE` | `"qrcode"` |
| `lvgl.BOX` | `"box"` |
| `lvgl.BUTTON` | `"button"` |
| `lvgl.MOMENTARY_BUTTON` | `"momentaryButton"` |
| `lvgl.TOGGLE` | `"toggle"` |
| `lvgl.TEXT_EDIT` | `"textEdit"` |
| `lvgl.NUMBER_EDIT` | `"numberEdit"` |
| `lvgl.CHOICE` | `"choice"` |
| `lvgl.SLIDER` | `"slider"` |
| `lvgl.VERTICAL_SLIDER` | `"verticalSlider"` |
| `lvgl.PAGE` | `"page"` |
| `lvgl.FONT` | `"font"` |
| `lvgl.ALIGN` | `"align"` |
| `lvgl.COLOR` | `"color"` |
| `lvgl.TIMER` | `"timer"` |
| `lvgl.SWITCH` | `"switch"` |
| `lvgl.SOURCE` | `"source"` |
| `lvgl.FILE` | `"file"` |
| `lvgl.SETTING` | `"setting"` |
