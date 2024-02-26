---
description: >-
  Function returns colorFlag in RGB565 format that can be used with lcd draw
  functions.
---

# lcd.RGB

### Description

Returns colorFlag in RGB565 format that can be used with lcd draw functions.

### Syntax

**lcd.RGB( r, g, b | rgb )**

### Parameters

<table><thead><tr><th width="109">Name</th><th width="99" data-type="checkbox">Required</th><th width="115">Type</th><th>Description</th></tr></thead><tbody><tr><td>r</td><td>true</td><td>integer</td><td>number between 0 (0x00) and 255 (0xFF) that expresses te amount of red in the color</td></tr><tr><td>g</td><td>true</td><td>interer</td><td>number between (0x00) and 255 (0xFF) that expresses te amount of green in the color</td></tr><tr><td>b</td><td>true</td><td>integer</td><td>number between (0x00) and 255 (0xFF)that expresses te amount of blue in the color</td></tr></tbody></table>

or

<table><thead><tr><th width="109">Name</th><th width="99" data-type="checkbox">Required</th><th width="115">Type</th><th>Description</th></tr></thead><tbody><tr><td>rgb</td><td>true</td><td>integer</td><td>number between 0 (0x00) and 16777215 (0xFFFFFF) that expresses the RGB value (0xFF0000=RED, 0x00FF00=GREEN, 0x0000FF=BLUE)</td></tr></tbody></table>

### Returns

* `color_flag`.   See [Drawing Flags](../../lua-api-programming/drawing-flags-and-colors.md)

### Notes

### Available on

* [ ] [B\&W LCD radios](../../overview/radios/#radios-with-b-and-w-lcd-screen)
* [ ] [Grayscale LCD radios](../../overview/radios/#radios-with-grayscale-lcd-screen)
* [x] [Color LCD radios](../../overview/radios/#radios-with-color-lcd-screen)

### API status

<table><thead><tr><th width="166">EdgeTX version</th><th width="573">Action</th></tr></thead><tbody><tr><td>2.3.0</td><td>Introduced</td></tr></tbody></table>

### Examples&#x20;

{% tabs %}
{% tab title="Example 1" %}
```lua
-- RGB numeric parameters
local darkred = lcd.RGB(20,0,0)  -- create color_flag for color
lcd.drawText(0,0,"Very dark red text", darkred)
```
{% endtab %}

{% tab title="Example 2" %}
```lua
-- RGB hex parameter
local mygrey = lcd.RGB(0xAEAEAE)  -- create color_flag for color
lcd.drawText(0,20,"My grey color", mygrey)
```
{% endtab %}
{% endtabs %}

### Related topics

* [Drawing flag](../../lua-api-programming/drawing-flags-and-colors.md)
* [Color constants](../constants/color-constants.md)
