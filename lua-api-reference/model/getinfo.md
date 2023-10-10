# model.getInfo

## Description

Gets currently selected Model's information

## Syntax

model.getInfo()

## Parameters

none

## Return values

`table` containing model information with following fields:

<table data-header-hidden><thead><tr><th width="178">Field</th><th width="102">Type</th><th>Decription</th></tr></thead><tbody><tr><td><strong>name</strong></td><td>string</td><td>Model's name set.  </td></tr><tr><td><strong>filename</strong></td><td>string</td><td>Name of <a data-footnote-ref href="#user-content-fn-1">&#x3C;<mark style="color:purple;">???></mark></a></td></tr><tr><td><strong>bitmap</strong></td><td>string</td><td>Name of model's picture file located on SD Card in /IMAGES/ folder</td></tr><tr><td><strong>extendedLimits</strong></td><td>boolean</td><td><code>true</code> if extended limits are enabled otherwise <code>false</code></td></tr><tr><td><strong>jitterFilter</strong></td><td>number</td><td><a data-footnote-ref href="#user-content-fn-2">model level ADC filter</a></td></tr></tbody></table>

{% hint style="warning" %}
**bitmap** field is not available on BW radios
{% endhint %}

## API Status

<table><thead><tr><th width="153"></th><th width="100" data-type="checkbox">Available</th><th width="168" data-type="select">Status</th><th>Comment</th></tr></thead><tbody><tr><td>BW radios</td><td>true</td><td></td><td></td></tr><tr><td>Color radios</td><td>true</td><td></td><td></td></tr></tbody></table>

## Change log

<table><thead><tr><th width="179">EdgeTX version</th><th>Change</th></tr></thead><tbody><tr><td>2.4.0</td><td>Introduced</td></tr><tr><td>2.6.0</td><td>added <code>filename</code> to return value table.</td></tr><tr><td>2.8.0</td><td>added <code>extendedLimits</code> , <code>jitterFilter</code>, <code>labels</code> to return value table.</td></tr></tbody></table>

## Examples

Displaying model's name

```lua
local modelInfo -- declare variable available to all functions 

local function my_init() {
    modelInfo = model.getInfo() -- read model's info table
}

local function my_run(event) {
    lcd.clear()
    lcd.drawText(0, 0, modelInfo.name) -- display model's name
    return 0
}

return { run = my_run, init = my_init }
```

Displaying model's all information

```lua
local modelInfo -- declare variable available to all functions 
local lineHeight = 8 -- for color radios change to 16

local function my_init() {
    modelInfo = model.getInfo() -- read model's info table
}

local function my_run(event) {
    lcd.clear()
    local y = 0
    for fieldName, fieldValue in pairs(modelInfo) do
        lcd.drawText( 0, y, fieldName .. ": " .. tostring(fieldValue) ) -- display model's name
        y = y + lineHeight
    end
    return 0
}

return { run = my_run, init = my_init }
```

Displaying model's information

[^1]: <mark style="color:red;">Name of what?</mark>    &#x20;

[^2]: <mark style="color:red;">What values are allowed?</mark>     &#x20;
