# lcd.clear( \[color] )

### Description

Clears the LCD screen

### Parameters

* `color_flag` (optional), see [Drawing Flags](../../lua-api-programming/drawing-flags-and-colors.md)

### Returns

none

### Notes

This function works only in stand-alone and telemetry & widget scripts. See [script types](../../overview/script-types/).

### Available on

* [x] [B\&W LCD radios](../../overview/radios/#radios-with-b-and-w-lcd-screen)
* [x] [Grayscale LCD radios](../../overview/radios/#radios-with-grayscale-lcd-screen)
* [x] [Color LCD radios](../../overview/radios/#radios-with-color-lcd-screen)

### API status

<table><thead><tr><th width="166">EdgeTX version</th><th width="573">Action</th></tr></thead><tbody><tr><td>2.3.0</td><td>Introduced</td></tr></tbody></table>

### Examples&#x20;

{% tabs %}
{% tab title="Example 1" %}
```lua
-- clearing lcd with default color
lcd.clear()
```
{% endtab %}

{% tab title="Example 2" %}
```lua
-- clearing lcd screen to dark red
local darkred = lcd.RGB(20,0,0)  -- create color_flag for color
lcd.clear(darkred)
```
{% endtab %}
{% endtabs %}

### Related topics

* [Drawing flag](../../lua-api-programming/drawing-flags-and-colors.md)
* [Color constants](../constants/color-constants.md)
