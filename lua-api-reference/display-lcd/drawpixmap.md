---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/Ly8RKETivxoHMb7Zzqkb/lua-api-reference/display-lcd/drawpixmap
---

# lcd.drawPixmap

Draws a bitmap file stored on the SD card at `(x, y)`.

### Syntax

#### lcd.drawPixmap( x, y, name )

### Parameters

<table><thead><tr><th width="109">Name</th><th width="61" data-type="checkbox">Req</th><th width="146">Type</th><th>Description</th></tr></thead><tbody><tr><td>x</td><td>true</td><td>integer</td><td>top coordinate</td></tr><tr><td>y</td><td>true</td><td>integer</td><td>left coordinate</td></tr><tr><td>name</td><td>true</td><td>string</td><td>full path to a bitmap on the SD card, e.g. <code>"/IMAGES/test.bmp"</code></td></tr></tbody></table>

### Returns

none

### Notes

{% hint style="info" %}
Maximum image size is `[LCD_W / 2] x [LCD_H]` pixels.
{% endhint %}

{% hint style="info" %}
If you draw the same image repeatedly, prefer loading it once with [`Bitmap.open`](https://app.gitbook.com/s/Ly8RKETivxoHMb7Zzqkb/lua-api-reference/bitmap/open) and then drawing it with [`lcd.drawBitmap`](https://app.gitbook.com/s/Ly8RKETivxoHMb7Zzqkb/lua-api-reference/display-lcd/drawbitmap).
{% endhint %}

### Available on

* [ ] [B\&W LCD radios](https://app.gitbook.com/s/Ly8RKETivxoHMb7Zzqkb/overview/radios#radios-with-b-and-w-lcd-screen)
* [x] [Grayscale LCD radios](https://app.gitbook.com/s/Ly8RKETivxoHMb7Zzqkb/overview/radios#radios-with-grayscale-lcd-screen)
* [ ] [Color LCD radios](https://app.gitbook.com/s/Ly8RKETivxoHMb7Zzqkb/overview/radios#radios-with-color-lcd-screen)

### API status

<table><thead><tr><th width="166">EdgeTX version</th><th width="573">Action</th></tr></thead><tbody><tr><td>2.0.0</td><td>Introduced</td></tr></tbody></table>

### Examples

{% tabs %}
{% tab title="Example 1" %}
```lua
-- draw bitmap file stored on the SD card
lcd.drawPixmap(10, 10, "/IMAGES/test.bmp")
```
{% endtab %}

{% tab title="Example 2" %}
```lua
-- draw at the top-left corner
lcd.drawPixmap(0, 0, "/IMAGES/test.bmp")
```
{% endtab %}
{% endtabs %}

### Related topics

* [`lcd.drawBitmap`](https://app.gitbook.com/s/Ly8RKETivxoHMb7Zzqkb/lua-api-reference/display-lcd/drawbitmap)
* [`Bitmap.open`](https://app.gitbook.com/s/Ly8RKETivxoHMb7Zzqkb/lua-api-reference/bitmap/open)
* [Screen Constants](https://app.gitbook.com/s/Ly8RKETivxoHMb7Zzqkb/lua-api-reference/constants/screen-constants)
