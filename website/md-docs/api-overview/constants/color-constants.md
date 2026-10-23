---
description: >-
  On radios with color display, a color may be added to the flags described
  above.
---

# Color Constants

There are two types of color constants: one that is an index into a table holding a palette of theme colors, and one that is just a color.

## Indexed colors

These are the theme colors plus CUSTOM\_COLOR, and they can be changed with the function lcd.setColor\(color\_index, color\).

!!! note

    If an indexed color is changed, it changes everywhere that it is used. For the theme colors, this is not only in other widgets, but everywhere throughout the radio's user interface.

| Color constant name | Default theme color |
| :--- | :--- |
| `COLOR_THEME_PRIMARY1` | <span style="display:inline-block; width:1.5rem; height:1.5rem; background:#000000; border:1px solid #cbd5e1; border-radius:0.2rem; vertical-align:middle;"></span> |
| `COLOR_THEME_PRIMARY2` | <span style="display:inline-block; width:1.5rem; height:1.5rem; background:#ffffff; border:1px solid #cbd5e1; border-radius:0.2rem; vertical-align:middle;"></span> |
| `COLOR_THEME_PRIMARY3` | <span style="display:inline-block; width:1.5rem; height:1.5rem; background:#0c3f66; border:1px solid #cbd5e1; border-radius:0.2rem; vertical-align:middle;"></span> |
| `COLOR_THEME_SECONDARY1` | <span style="display:inline-block; width:1.5rem; height:1.5rem; background:#125e99; border:1px solid #cbd5e1; border-radius:0.2rem; vertical-align:middle;"></span> |
| `COLOR_THEME_SECONDARY2` | <span style="display:inline-block; width:1.5rem; height:1.5rem; background:#b6e0f2; border:1px solid #cbd5e1; border-radius:0.2rem; vertical-align:middle;"></span> |
| `COLOR_THEME_SECONDARY3` | <span style="display:inline-block; width:1.5rem; height:1.5rem; background:#e4eef2; border:1px solid #cbd5e1; border-radius:0.2rem; vertical-align:middle;"></span> |
| `COLOR_THEME_FOCUS` | <span style="display:inline-block; width:1.5rem; height:1.5rem; background:#14a1e5; border:1px solid #cbd5e1; border-radius:0.2rem; vertical-align:middle;"></span> |
| `COLOR_THEME_EDIT` | <span style="display:inline-block; width:1.5rem; height:1.5rem; background:#009909; border:1px solid #cbd5e1; border-radius:0.2rem; vertical-align:middle;"></span> |
| `COLOR_THEME_ACTIVE` | <span style="display:inline-block; width:1.5rem; height:1.5rem; background:#ffde00; border:1px solid #cbd5e1; border-radius:0.2rem; vertical-align:middle;"></span> |
| `COLOR_THEME_WARNING` | <span style="display:inline-block; width:1.5rem; height:1.5rem; background:#e00000; border:1px solid #cbd5e1; border-radius:0.2rem; vertical-align:middle;"></span> |
| `COLOR_THEME_DISABLED` | <span style="display:inline-block; width:1.5rem; height:1.5rem; background:#8c8c8c; border:1px solid #cbd5e1; border-radius:0.2rem; vertical-align:middle;"></span> |
| `CUSTOM_COLOR` | <span style="display:inline-block; width:1.5rem; height:1.5rem; background:#aa5500; border:1px solid #cbd5e1; border-radius:0.2rem; vertical-align:middle;"></span> |

## Literal colors

These color constants cannot be changed:

| Color constant name | Fixed color |
| :--- | :--- |
| `BLACK` | <span style="display:inline-block; width:1.5rem; height:1.5rem; background:#000000; border:1px solid #cbd5e1; border-radius:0.2rem; vertical-align:middle;"></span> |
| `WHITE` | <span style="display:inline-block; width:1.5rem; height:1.5rem; background:#ffffff; border:1px solid #cbd5e1; border-radius:0.2rem; vertical-align:middle;"></span> |
| `LIGHTWHITE` | <span style="display:inline-block; width:1.5rem; height:1.5rem; background:#eaeaea; border:1px solid #cbd5e1; border-radius:0.2rem; vertical-align:middle;"></span> |
| `YELLOW` | <span style="display:inline-block; width:1.5rem; height:1.5rem; background:#ffff00; border:1px solid #cbd5e1; border-radius:0.2rem; vertical-align:middle;"></span> |
| `BLUE` | <span style="display:inline-block; width:1.5rem; height:1.5rem; background:#0000ff; border:1px solid #cbd5e1; border-radius:0.2rem; vertical-align:middle;"></span> |
| `DARKBLUE` | <span style="display:inline-block; width:1.5rem; height:1.5rem; background:#0000a0; border:1px solid #cbd5e1; border-radius:0.2rem; vertical-align:middle;"></span> |
| `GREY` | <span style="display:inline-block; width:1.5rem; height:1.5rem; background:#606060; border:1px solid #cbd5e1; border-radius:0.2rem; vertical-align:middle;"></span> |
| `DARKGREY` | <span style="display:inline-block; width:1.5rem; height:1.5rem; background:#404040; border:1px solid #cbd5e1; border-radius:0.2rem; vertical-align:middle;"></span> |
| `LIGHTGREY` | <span style="display:inline-block; width:1.5rem; height:1.5rem; background:#c0c0c0; border:1px solid #cbd5e1; border-radius:0.2rem; vertical-align:middle;"></span> |
| `RED` | <span style="display:inline-block; width:1.5rem; height:1.5rem; background:#ff0000; border:1px solid #cbd5e1; border-radius:0.2rem; vertical-align:middle;"></span> |
| `DARKRED` | <span style="display:inline-block; width:1.5rem; height:1.5rem; background:#a00000; border:1px solid #cbd5e1; border-radius:0.2rem; vertical-align:middle;"></span> |
| `GREEN` | <span style="display:inline-block; width:1.5rem; height:1.5rem; background:#00ff00; border:1px solid #cbd5e1; border-radius:0.2rem; vertical-align:middle;"></span> |
| `DARKGREEN` | <span style="display:inline-block; width:1.5rem; height:1.5rem; background:#00a000; border:1px solid #cbd5e1; border-radius:0.2rem; vertical-align:middle;"></span> |
| `LIGHTBROWN` | <span style="display:inline-block; width:1.5rem; height:1.5rem; background:#9c6d20; border:1px solid #cbd5e1; border-radius:0.2rem; vertical-align:middle;"></span> |
| `DARKBROWN` | <span style="display:inline-block; width:1.5rem; height:1.5rem; background:#6a4810; border:1px solid #cbd5e1; border-radius:0.2rem; vertical-align:middle;"></span> |
| `BRIGHTGREEN` | <span style="display:inline-block; width:1.5rem; height:1.5rem; background:#00b43c; border:1px solid #cbd5e1; border-radius:0.2rem; vertical-align:middle;"></span> |
| `ORANGE` | <span style="display:inline-block; width:1.5rem; height:1.5rem; background:#e5641e; border:1px solid #cbd5e1; border-radius:0.2rem; vertical-align:middle;"></span> |

## Deprecated color constants

These should no longer be used, but they are included for backwards compatibility. The old OpenTX API had a large number of indexed theme colors, and these have been mapped to the new theme colors as follows:

| Deprecated constant | Replacement |
| :--- | :--- |
| `ALARM_COLOR` | `COLOR_THEME_WARNING` |
| `BARGRAPH_BGCOLOR` | `COLOR_THEME_SECONDARY3` |
| `BARGRAPH1_COLOR` | `COLOR_THEME_SECONDARY1` |
| `BARGRAPH2_COLOR` | `COLOR_THEME_SECONDARY2` |
| `CURVE_AXIS_COLOR` | `COLOR_THEME_SECONDARY2` |
| `CURVE_COLOR` | `COLOR_THEME_SECONDARY1` |
| `CURVE_CURSOR_COLOR` | `COLOR_THEME_WARNING` |
| `HEADER_BGCOLOR` | `COLOR_THEME_FOCUS` |
| `HEADER_COLOR` | `COLOR_THEME_SECONDARY1` |
| `HEADER_CURRENT_BGCOLOR` | `COLOR_THEME_FOCUS` |
| `HEADER_ICON_BGCOLOR` | `COLOR_THEME_SECONDARY1` |
| `LINE_COLOR` | `COLOR_THEME_PRIMARY3` |
| `MAINVIEW_GRAPHICS_COLOR` | `COLOR_THEME_SECONDARY1` |
| `MAINVIEW_PANES_COLOR` | `COLOR_THEME_PRIMARY2` |
| `MENU_TITLE_BGCOLOR` | `COLOR_THEME_SECONDARY1` |
| `MENU_TITLE_COLOR` | `COLOR_THEME_PRIMARY2` |
| `MENU_TITLE_DISABLE_COLOR` | `COLOR_THEME_PRIMARY3` |
| `OVERLAY_COLOR` | `COLOR_THEME_PRIMARY1` |
| `SCROLLBOX_COLOR` | `COLOR_THEME_SECONDARY3` |
| `TEXT_BGCOLOR` | `COLOR_THEME_SECONDARY3` |
| `TEXT_COLOR` | `COLOR_THEME_SECONDARY1` |
| `TEXT_DISABLE_COLOR` | `COLOR_THEME_DISABLED` |
| `TEXT_INVERTED_BGCOLOR` | `COLOR_THEME_FOCUS` |
| `TEXT_INVERTED_COLOR` | `COLOR_THEME_PRIMARY2` |
| `TITLE_BGCOLOR` | `COLOR_THEME_SECONDARY1` |
| `TRIM_BGCOLOR` | `COLOR_THEME_FOCUS` |
| `TRIM_SHADOW_COLOR` | `COLOR_THEME_PRIMARY1` |
| `WARNING_COLOR` | `COLOR_THEME_WARNING` |
