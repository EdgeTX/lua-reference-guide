# lcd.drawBitmap

Displays prevoiusly loaded bitmap at (x,y) and optionally scales it.

### Syntax

#### lcd.drawBitmap( bitmap, x, y \[, scale] )

### Parameters

<table><thead><tr><th width="109">Name</th><th width="61" data-type="checkbox">Req</th><th width="146">Type</th><th>Description</th></tr></thead><tbody><tr><td>bitmap</td><td>true</td><td>bitmapPointer</td><td>stored in variable pointer to a bitmap previously opened with <a href="../bitmap/open.md">Bitmap.open</a></td></tr><tr><td>x</td><td>true</td><td>integer</td><td>top coordinate</td></tr><tr><td>y</td><td>true</td><td>integer</td><td>left coordinate</td></tr><tr><td>scale</td><td>false</td><td>integer (0-100)</td><td>scale in percent ie. 50 divides size by two, 100 displays bitmap in original size, 200 doubles size.</td></tr></tbody></table>

### Returns

none

### Notes

{% hint style="info" %}
Omitting scale draws image in 1:1 scale and is faster than specifying 100 for scale parameter.
{% endhint %}

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
-- drawing bitmap stored on sd card root folder with original size
local myLogo = Bitmap.open("/logo.png")
lcd.drawBitmap(myLogo,10,10)
```
{% endtab %}

{% tab title="Example 2" %}
```lua
-- drawing bitmap stored on sd card root folder doubling its size
local myLogo = Bitmap.open("/logo.png")
lcd.drawBitmap(myLogo,10,10,200)
```
{% endtab %}
{% endtabs %}

### Related topics

* [Drawing flag](../../lua-api-programming/drawing-flags-and-colors.md)
* [Color constants](../constants/color-constants.md)
* [Bitmap.open](../bitmap/open.md)

