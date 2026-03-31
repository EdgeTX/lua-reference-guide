---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/Ly8RKETivxoHMb7Zzqkb/lua-api-reference/display-lcd/lcd.drawtextlines
---

# lcd.drawTextLines(x, y, w, h, text \[, flags])

Draw text inside rectangle (x,y,w,h) with line breaks

### Parameters

* `x,y` (positive numbers) starting coordinate
* `w,h` (positive numbers) width and height of bounding rectangle
* `text` (string) text to display
* `flags` (optional) please see [Lcd functions overview](https://github.com/EdgeTX/lua-reference-guide/blob/main/lua_api_reference/lcd/lcd_functions-overview.html) for drawing flags and colors, and [Appendix](../../appendix/fonts.md) for available characters in each font set. RIGHT, CENTER and VCENTER are not implemented.

### Return value

* x,y (integers) point where text drawing ended

### Notes

### Available on

* [ ] [B\&W LCD radios](../../overview/radios/#radios-with-b-and-w-lcd-screen)
* [ ] [Grayscale LCD radios](../../overview/radios/#radios-with-grayscale-lcd-screen)
* [x] [Color LCD radios](../../overview/radios/#radios-with-color-lcd-screen)

### API status

<table><thead><tr><th width="166">EdgeTX version</th><th width="573">Action</th></tr></thead><tbody><tr><td>2.5.0</td><td>Introduced</td></tr><tr><td>2.11.0</td><td>x,y return added</td></tr></tbody></table>

### Examples

{% tabs %}
{% tab title="Example 1" %}
```lua
local y
_, y = lcd.drawTextLines(1, 0, 100, 40, "No TxGPS detected!", LEFT + TEXT_COLOR)
lcd.drawTextLines(1, y, 100, 100, "Make sure your firmware has GPS support enabled", LEFT + TEXT_COLOR)

```
{% endtab %}

{% tab title="Example 2" %}

{% endtab %}
{% endtabs %}
