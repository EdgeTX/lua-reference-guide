---
description: Build a complex UI in a single operation.
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/Ly8RKETivxoHMb7Zzqkb/lua-api-reference/lvgl-for-lua/lvgl.build
---

# lvgl.build

## Syntax

lvgl.build(\[parent], \{{settings\}})

parent:build(\{{settings\}})

## Parameters

See the API page for parameter description and common settings.

Build specific settings:

<table><thead><tr><th width="127">Name</th><th>Type</th><th>Description</th><th>Default if not set</th></tr></thead><tbody><tr><td>type</td><td>String or type constant</td><td>Mandatory on each table entry to determine what type of LVGL object to create.<br><br>e.g.<br>  type="rectangle"<br>  type=lvgl.RECTANGLE</td><td></td></tr><tr><td>name</td><td>String</td><td></td><td>Empty string</td></tr><tr><td>children</td><td>Table</td><td></td><td>nil</td></tr></tbody></table>

## Return values

Table of named LVGL objects.

## Notes

The 'settings' parameter to lvgl.build should be a table of tables. Each inner table creates a separate LVGL object based on the 'type' value.

For example the code below creates two object, a label and a rectangle.

```lua
lvgl.build({
    {type="label", x=0, y=0, text="Some text", color=BLACK},
    {type="rectangle", x=0, y=20, w=100, h=100, color=BLACK}
})
```

Objects can be nested by using the 'children' setting, this should be another table of tables just like the build settings.

For example this code creates another label as a child of the rectangle object. The x & y co-ordinates for the second label are relative to the top left corner of the parent rectangle.

```lua
lvgl.build({
    {type="label", x=0, y=0, text="Some text", color=BLACK},
    {type="rectangle", x=0, y=20, w=100, h=100, color=BLACK,
        children={
            {type="label", x=5, y=5, text="More text", color=BLACK}
        }
    }
})
```

The lvgl.build function will return a table of LVGL objects. This table will contain named references to any objects created that have the 'name' setting, Only references to named objects are returned.

For example this code assigns a name to the inner label and then updates the color.

```lua
local uiElements = lvgl.build({
    {type="label", x=0, y=0, text="Some text", color=BLACK},
    {type="rectangle", x=0, y=20, w=100, h=100, color=BLACK,
        children={
            {type="label", x=5, y=5, text="More text", color=BLACK, name="lbl1"}
        }
    }
})

uiElements["lbl1"]:set({color=BLUE})
```

## Warning

Very large nested tables or very deeply nested tables may not work when compiled to a .luac script. If your script works when run from the .lua file; but fails when run from .luac, try breaking the lvgl.build call into multiple calls with smaller tables.

## API Status

<table><thead><tr><th width="153"></th><th width="72" data-type="checkbox">Avail</th><th width="145">Status<select><option value="93c8b010d44e45efaec5c0c14d3992ac" label="active" color="blue"></option><option value="7e7074d1164048e3b0b24a02b4300f6c" label="to be depreciated" color="blue"></option></select></th><th>Comment</th></tr></thead><tbody><tr><td>BW radios</td><td>false</td><td></td><td></td></tr><tr><td>Color radios</td><td>true</td><td><span data-option="93c8b010d44e45efaec5c0c14d3992ac">active</span></td><td></td></tr></tbody></table>

## Change log

<table><thead><tr><th width="177">EdgeTX version</th><th>Change</th></tr></thead><tbody><tr><td>2.11.0</td><td>Introduced</td></tr></tbody></table>
