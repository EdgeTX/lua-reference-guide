---
description: This section will give some technical details for radios with a color screen.
---

# Drawing Flags and Colors

An  argument with drawing flags can be given to the various functions that draw on the LCD screen. The lower half of the flags \(bits 1-16\) are the flag attributes shown below, and the upper half of the flags \(bits 17-32\) are a color value.

Not all of the flags below should be directly manipulated from Lua, but those that are meant to be set directly by Lua, are accessible by the [Lua flag constants](../part_iii_-_opentx_lua_api_reference/constants/flags-and-pattern-constants.md#flags).

![](../.gitbook/assets/flags%20%281%29.png)

Since the flags are bits, you can add them up to combine, as long as you only add each flag _one_ time. If you add the same flag twice, then it will add up to the next bit over, e.g. `INVERS + INVERS = VCENTER`. If you want to add a flag to a value where it may already be set, then use `flags = bit32.bor(flags, INVERS)`.

RGB\_FLAG decides how the color value is encoded into the upper half \(bits 17-32\). 

If RGB\_FLAG = 0, then an index into a color table is stored. This color table holds a default color \(index 0\), the theme colors, and CUSTOM\_COLOR. The entries in the color table can be changed with the function [`lcd.setColor`](../part_iii_-_opentx_lua_api_reference/lcd-functions-less-than-greater-than-luadoc-begin-lcd/setcolor.md). The advantage of this system is that the color changes everywhere that this indexed color is used, and this is how different color themes are created. **Notice that changing the theme colors affects the entire user interface of your radio!!**

If RGB\_FLAG = 1, then a 16-bit RGB565 color is stored. This is used directly by the system to draw a color on the screen.

You should not change RGB\_FLAG explicitly; this is handled automatically by the various functions and Lua constants. But you should be aware of the following.

* [`lcd.setColor`](../part_iii_-_opentx_lua_api_reference/lcd-functions-less-than-greater-than-luadoc-begin-lcd/setcolor.md) must have an [indexed color](../part_iii_-_opentx_lua_api_reference/constants/color-constants.md#indexed-colors) as its first argument, because this will be the index of the color in the table being changed. Giving another color, e.g. ORANGE, as the first argument will result in nothing.
* If no color is given to the flags with a drawing function, RGB\_FLAGS = 0 and the color index = 0. Therefore, the default color is stored in the color table under this index, and you can change the default color with `lcd.setColor(0, color)`.
* [`lcd.getColor` ](../part_iii_-_opentx_lua_api_reference/lcd-functions-less-than-greater-than-luadoc-begin-lcd/getcolor.md)always returns a RGB color. This can be used to "save" an indexed color before you change it.
* [`lcd.RGB`](../part_iii_-_opentx_lua_api_reference/lcd-functions-less-than-greater-than-luadoc-begin-lcd/rgb.md) obviously returns a RGB color.

### Colors in EdgeTX versus OpenTX

OpenTX only supports indexed colors in drawing functions, so you must first call `lcd.setColor` to change e.g. CUSTOM\_COLOR, and then call the LCD drawing function with that indexed color. In EdgeTX, you can use either type of color for drawing functions, so you are no longer forced to constantly call `lcd.setColor`. You can also store any color in local variables, and then use these when drawing, thus effectively creating your own color theme.

In OpenTX, `lcd.RGB` returns a 16 bit RGB565 value, but in EdgeTX it returns a 32 bit flags value with the 16 bit RGB565 value in the upper half \(bits 17-32\). Therefore, colors in EdgeTX are not binary compatible with colors in OpenTX. But if you use the functions `lcd.RGB`, `lcd.setColor`, and `lcd.getColor`, then your code should work the same way in EdgeTX as in OpenTX.

Unfortunately, OpenTX has disabled the function `lcd.RGB` when the screen is not available for drawing, so it can only be called successfully from the `refresh` function in widgets and from the `run` function in One-Time scripts. Therefore, some existing widget scripts set up colors with hard coded constants instead of calling `lcd.RGB` during initialization, and this is not going to work with EdgeTX, because of the different binary format.

A pull request has been submitted to OpenTX, allowing `lcd.RGB` to work also during widget script initialization, and hopefully, it will be merged into OpenTX 2.3.15. If that happens, then the obvious way to solve the problem is to use `lcd.RGB` values instead of hard coded color constants. But in the meantime, the following RGB function can be used for setting up colors in a way that works for both EdgeTX and OpenTX.

```lua
local function RGB(r, g, b)
  local rgb = lcd.RGB(r, g, b)
  
  if not rgb then
    rgb = bit32.lshift(bit32.rshift(bit32.band(r, 0xFF), 3), 11)
    rgb = rgb + bit32.lshift(bit32.rshift(bit32.band(g, 0xFF), 2), 5)
    rgb = rgb + bit32.rshift(bit32.band(b, 0xFF), 3)
  end
  
  return rgb
end
```

This functions calls `lcd.RGB`, and if it gets a nil value \(because we are running a widget script under OpenTX, and it is not called from the `refresh` function\) then it creates the 16-bit RGB565 value that OpenTX wants.

