# model.getCurve(curve)

Deletes line from specified Input of curently selected model.

## Syntax

model.getCurve( curveID )

## Parameters

<table><thead><tr><th width="157.33333333333331">Name</th><th width="124">Type</th><th width="64" data-type="checkbox">Req</th><th>Description</th></tr></thead><tbody><tr><td><strong>curveID</strong></td><td>number</td><td>true</td><td>Curve ID number. Normal Lua index.  <br>Use 1 for curve 1, 8 for Input 8 etc.</td></tr></tbody></table>

## Return values

## Return values

`table` containing model information with following fields:

<table data-header-hidden><thead><tr><th width="178">Field</th><th width="102">Type</th><th>Decription</th></tr></thead><tbody><tr><td><strong>name</strong></td><td>string</td><td>Model's name set.  </td></tr><tr><td><strong>filename</strong></td><td>string</td><td>Name of <a data-footnote-ref href="#user-content-fn-1">&#x3C;<mark style="color:purple;">???></mark></a></td></tr><tr><td><strong>bitmap</strong></td><td>string</td><td>Name of model's picture file located on SD Card in /IMAGES/ folder</td></tr><tr><td><strong>extendedLimits</strong></td><td>boolean</td><td><code>true</code> if extended limits are enabled otherwise <code>false</code></td></tr><tr><td><strong>jitterFilter</strong></td><td>number</td><td><a data-footnote-ref href="#user-content-fn-2">model level ADC filter</a></td></tr></tbody></table>

{% hint style="warning" %}
**bitmap** field is not available on BW radios
{% endhint %}

## API Status

`table` containing model information with following fields:

`table` containing model information with following fields:





## API Status

<table><thead><tr><th width="161"></th><th width="72" data-type="checkbox">Avail</th><th width="145" data-type="select">Status</th><th>Comment</th></tr></thead><tbody><tr><td>BW radios</td><td>true</td><td></td><td></td></tr><tr><td>Color radios</td><td>true</td><td></td><td></td></tr></tbody></table>

## Change log

<table><thead><tr><th width="177">EdgeTX version</th><th>Change</th></tr></thead><tbody><tr><td>2.4.0</td><td>Introduced</td></tr></tbody></table>

## Examples

Example description

```lua
-- sample script
```

Note this function uses Lua's usual index starting with 1 since version 2.9.0.

@status current Introduced in 2.0.12, uses Lua's normal indexing as of 2.9.0

## Parameters

* `curve` (unsigned number) curve number (use 0 for Curve1)

## Return value

* `nil` requested curve does not exist
* `table` curve data:
  * `name` (string) name
  * `type` (number) type
  * `smooth` (boolean) smooth
  * `points` (number) number of points
  * `y` (table) table of Y values:
    * `key` is point number (zero based)
    * `value` is y value
  * `x` (table) **only included for custom curve type**:
    * `key` is point number (zero based)
    * `value` is x value

[^1]: <mark style="color:red;">Name of what?</mark>    &#x20;

[^2]: <mark style="color:red;">What values are allowed?</mark>     &#x20;
