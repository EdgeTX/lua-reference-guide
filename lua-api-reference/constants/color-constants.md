---
description: >-
  On radios with color display, a color may be added to the flags described
  above.
---

# Color Constants

There are two types of color constants: one that is an index into a table holding a palette of theme colors, and one that is just a color.

## Indexed colors

These are the theme colors plus CUSTOM\_COLOR, and they can be changed with the function lcd.setColor\(color\_index, color\). **Please note: if an indexed color is changed, then it changes everywhere that it is used. For the theme colors, this is not only in other widgets, but everywhere throughout the radio's user interface!**

* COLOR\_THEME\_PRIMARY1
* COLOR\_THEME\_PRIMARY2
* COLOR\_THEME\_PRIMARY3
* COLOR\_THEME\_SECONDARY1
* COLOR\_THEME\_SECONDARY2
* COLOR\_THEME\_SECONDARY3
* COLOR\_THEME\_FOCUS
* COLOR\_THEME\_EDIT
* COLOR\_THEME\_ACTIVE
* COLOR\_THEME\_WARNING
* COLOR\_THEME\_DISABLED
* CUSTOM\_COLOR

## Literal colors

These color constants cannot be changed:

* BLACK
* WHITE
* LIGHTWHITE
* YELLOW
* BLUE
* DARKBLUE
* GREY
* DARKGREY
* LIGHTGREY
* RED
* DARKRED
* GREEN
* DARKGREEN
* LIGHTBROWN
* DARKBROWN
* BRIGHTGREEN
* ORANGE

## Deprecated color constants

These should no longer be used, but they are included for backwards compatibility. The old OpenTX API had a large number of indexed theme colors, and these have been mapped to the new theme colors as follows:

* ALARM\_COLOR -&gt; COLOR\_THEME\_WARNING
* BARGRAPH\_BGCOLOR -&gt; COLOR\_THEME\_SECONDARY3
* BARGRAPH1\_COLOR -&gt; COLOR\_THEME\_SECONDARY1
* BARGRAPH2\_COLOR -&gt; COLOR\_THEME\_SECONDARY2
* CURVE\_AXIS\_COLOR -&gt; COLOR\_THEME\_SECONDARY2
* CURVE\_COLOR -&gt; COLOR\_THEME\_SECONDARY1
* CURVE\_CURSOR\_COLOR -&gt; COLOR\_THEME\_WARNING
* HEADER\_BGCOLOR -&gt; COLOR\_THEME\_FOCUS
* HEADER\_COLOR -&gt; COLOR\_THEME\_SECONDARY1
* HEADER\_CURRENT\_BGCOLOR -&gt; COLOR\_THEME\_FOCUS
* HEADER\_ICON\_BGCOLOR -&gt; COLOR\_THEME\_SECONDARY1
* LINE\_COLOR -&gt; COLOR\_THEME\_PRIMARY3
* MAINVIEW\_GRAPHICS\_COLOR -&gt; COLOR\_THEME\_SECONDARY1
* MAINVIEW\_PANES\_COLOR -&gt; COLOR\_THEME\_PRIMARY2
* MENU\_TITLE\_BGCOLOR -&gt; COLOR\_THEME\_SECONDARY1
* MENU\_TITLE\_COLOR -&gt; COLOR\_THEME\_PRIMARY2
* MENU\_TITLE\_DISABLE\_COLOR -&gt; COLOR\_THEME\_PRIMARY3
* OVERLAY\_COLOR -&gt; COLOR\_THEME\_PRIMARY1
* SCROLLBOX\_COLOR -&gt; COLOR\_THEME\_SECONDARY3
* TEXT\_BGCOLOR -&gt; COLOR\_THEME\_SECONDARY3
* TEXT\_COLOR -&gt; COLOR\_THEME\_SECONDARY1
* TEXT\_DISABLE\_COLOR -&gt; COLOR\_THEME\_DISABLED
* TEXT\_INVERTED\_BGCOLOR -&gt; COLOR\_THEME\_FOCUS
* TEXT\_INVERTED\_COLOR -&gt; COLOR\_THEME\_PRIMARY2
* TITLE\_BGCOLOR -&gt; COLOR\_THEME\_SECONDARY1
* TRIM\_BGCOLOR -&gt; COLOR\_THEME\_FOCUS
* TRIM\_SHADOW\_COLOR -&gt; COLOR\_THEME\_PRIMARY1
* WARNING\_COLOR -&gt; COLOR\_THEME\_WARNING

