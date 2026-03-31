---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/Ly8RKETivxoHMb7Zzqkb/lua-api-reference/system/rgb
---

# screenshot()

Takes a screenshot, which is saved to the SCREENSHOTS folder on the radio SD card.

### Syntax

#### **`screenshot()`**

### Returns

* `None`

### Notes

This command is currently not rate limited, so repeated frequent calls will slow down the UI and can even freeze the entire radio, so should be used with care.

### Available on

* [x] [B\&W LCD radios](../../overview/radios/#radios-with-b-and-w-lcd-screen)
* [x] [Grayscale LCD radios](../../overview/radios/#radios-with-grayscale-lcd-screen)
* [x] [Color LCD radios](../../overview/radios/#radios-with-color-lcd-screen)

### API status

<table><thead><tr><th width="166">EdgeTX version</th><th width="573">Action</th></tr></thead><tbody><tr><td>2.11.0</td><td>Introduced</td></tr></tbody></table>

### Examples

{% tabs %}
{% tab title="Example 1" %}
```lua
-- Take a screenshot
screenshot()
```
{% endtab %}
{% endtabs %}

### Related topics

* [Drawing flag](../../lua-api-programming/drawing-flags-and-colors.md)
* [Color constants](../constants/color-constants.md)
