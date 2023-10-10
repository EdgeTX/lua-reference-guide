# model.getInfo

## Description

Get current Model information@status current Introduced in 2.0.6, changed in 2.2.0, filename added in 2.6.0, extendedLimits, jitterFilter, and labels added in 2.8.0

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



[^1]: <mark style="color:red;">Name of what?</mark>    &#x20;

[^2]: <mark style="color:red;">What values are allowed?</mark>     &#x20;
