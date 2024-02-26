# lcd.drawChannel(x, y, source, flags)

Display a telemetry value at (x,y)

@status current Introduced in 2.0.6, changed in 2.1.0 (only telemetry sources are valid)

### Parameters

* `x,y` (positive numbers) starting coordinate
* `source` can be a source identifier (number) or a source name (string). See getValue()
* `flags` (unsigned number) drawing flags

###

Draws channel value defined in source variable at (x,y)

### Syntax

#### lcd.drawChannel(x, y, source \[, flags])

### Parameters

<table><thead><tr><th width="109">Name</th><th width="61" data-type="checkbox">Req</th><th width="146">Type</th><th>Description</th></tr></thead><tbody><tr><td>x</td><td>true</td><td>integer</td><td>top coordinate</td></tr><tr><td>y</td><td>true</td><td>integer</td><td>left coordinate</td></tr><tr><td>source</td><td>true</td><td>integer (sourceID) or string (sourceName)</td><td>See Sou</td></tr><tr><td>flags</td><td>false</td><td>integer (drawingFlag)</td><td>See <a href="../../lua-api-programming/drawing-flags-and-colors.md">Drawing Flags</a> </td></tr></tbody></table>

### Returns

none

### Notes

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
-- example
```
{% endtab %}

{% tab title="Example 2" %}
```lua
-- example
```
{% endtab %}
{% endtabs %}
