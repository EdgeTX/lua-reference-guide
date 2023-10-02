---
description: >-
  Lua makes it easy to load and unload code modules on the fly, to save memory
  or to provide program extensions.
---

# Loading Code Modules Dynamically

The [`loadScript(<file>)`](../part_iii_-_opentx_lua_api_reference/general-functions-less-than-greater-than-luadoc-begin-general/loadscript.md) function will load a script from a the file and return a function that is the body of the script, as described in the previous section. So you could have the following Lua script file saved on the SD card:

```lua
-- /SCRIPTS/TestScript.lua
local c = ...

local function f(x)
  return x + c
end

return f
```

You can load and use the above file with the following code:

```lua
local chunk = loadScript("/SCRIPTS/TestScript.lua")

local f1 = chunk(1)
local y = f1(5)
-- y = 5 + 1

local f2 = chunk(3)
local z = f2(5)
-- z = 5 + 3
```

So here we put together what we learned in the previous section. The body of the script is an anonymous function returned by `loadScript` and stored in the variable `chunk`. It returns the function `f` when it is called. The local variable `c` in the script is assigned to the first _vararg_ passed to the call. Since a new closure is created every time we call `chunk`, `f1` and `f2` have different closures with different values of `c`.

