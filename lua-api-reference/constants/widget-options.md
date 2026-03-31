---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/Ly8RKETivxoHMb7Zzqkb/lua-api-reference/constants/widget-options
---

# Widget Options Constants

There are several option types that can be specified in the widget options table, which are exposed to the user via the Widget Settings menu.

<table><thead><tr><th width="191">Type</th><th>Description</th></tr></thead><tbody><tr><td>COLOR</td><td>Displays a color picker, returns a color flag value</td></tr><tr><td>BOOL</td><td>Displays a toggle/checkbox, value toggles between 0 and 1</td></tr><tr><td>STRING</td><td>Text input option, limited to 8 characters in 2.10 or earlier, 12 characters in 2.11.</td></tr><tr><td>TIMER</td><td>Choice option, lets you pick from available timers</td></tr><tr><td>SOURCE</td><td>Choice option, lets you pick from available sources (i.e. sticks, switches, LS)</td></tr><tr><td>SWITCH</td><td>Choice option to select from available switches.</td></tr><tr><td>VALUE</td><td>Numerical input option, can specify default, min and max value</td></tr><tr><td>TEXT_SIZE</td><td>Choice option, lets you pick from the available text sizes (i.e. small, large)</td></tr><tr><td>ALIGNMENT</td><td>Choice option, lets you pick from available alignment options (i.e. left, center, right)</td></tr><tr><td>SLIDER</td><td>Select numerical value using a slider control (available in 2.11)</td></tr><tr><td>CHOICE</td><td>Select numerical value using a custom popup list (available in 2.11)</td></tr><tr><td>FILE</td><td>Select a file from SD card / internal storage (available in 2.11). Filename is limited to 12 characters maximum.</td></tr></tbody></table>

{% hint style="warning" %}
Maximum five`options` are allowed.

Note: from 2.11 ten options are allowed per widget.
{% endhint %}

{% hint style="warning" %}
Option variable name's length **must be 10 characters or less and no spaces.**
{% endhint %}

## Example

```lua
-- Create a table with default options
-- Options can be changed by the user from the Widget Settings menu
-- Notice that each line is a table inside { }
local options = {
  { "Source", SOURCE, 1 },
  -- BOOL is actually not a boolean, but toggles between 0 and 1
  { "Boolean", BOOL, 1 },
  { "Value", VALUE, 1, 0, 10},
  { "Color", COLOR, ORANGE },
  { "Text", STRING, "Max8chrs" },
  { "File", FILE, "default", "PATH" }
}

```
