# Widget Options Constants

There are several option types that can be specified in the widget options table, which are exposed to the user via the Widget Settings menu.\
\
For example:

```
-- Create a table with default options
-- Options can be changed by the user from the Widget Settings menu
-- Notice that each line is a table inside { }
local options = {
  { "Source", SOURCE, 1 },
  -- BOOL is actually not a boolean, but toggles between 0 and 1
  { "Boolean", BOOL, 1 },
  { "Value", VALUE, 1, 0, 10},
  { "Color", COLOR, ORANGE },
  { "Text", STRING, "Max8chrs" }
}

```



| Type       | Description                                                                              |
| ---------- | ---------------------------------------------------------------------------------------- |
| COLOR      | Displays a color picker, returns a color flag value                                      |
| BOOL       | Displays a toggle/checkbox, value toggles between 0 and 1                                |
| STRING     | Text input option, limited to 8 characters                                               |
| TIMER      | Choice option, lets you pick from available timers                                       |
| SOURCE     | Choice option, lets you pick from available sources (i.e. sticks, switches, LS)          |
| VALUE      | Numerical input option, can specify default, min and max value                           |
| TEXT\_SIZE | Choice option, lets you pick from the available text sizes (i.e. small, large)           |
| ALIGNMENT  | Choice option, lets you pick from available alignment options (i.e. left, center, right) |
