# model.getCurve

Deletes line from specified Input of curently selected model.

## Syntax

model.getCurve( curveID )

## Parameters

<table><thead><tr><th width="136.47889908256883">Name</th><th width="124">Type</th><th width="64" data-type="checkbox">Req</th><th>Description</th></tr></thead><tbody><tr><td><strong>curveID</strong></td><td>number</td><td>true</td><td>Curve ID number. Normal Lua index.<br>Use 1 for curve 1, 8 for Input 8 etc.</td></tr></tbody></table>

## Return values

* `nil` requested curve does not exist
* `table` containing model information with following fields:

<table data-header-hidden><thead><tr><th width="147.38333333333333">Field</th><th width="102">Type</th><th>Decription</th></tr></thead><tbody><tr><td><code>name</code></td><td>string</td><td>Curve name</td></tr><tr><td><code>type</code></td><td>number</td><td>Curve type ID number<br>0 - ???<br>1 - ???<br>2 - ???</td></tr><tr><td><code>smooth</code></td><td>boolean</td><td><code>true</code> if curve is smoothed, otherwise <code>false</code></td></tr><tr><td><code>points</code></td><td>number</td><td>number of curve's points</td></tr><tr><td><code>y</code></td><td>table</td><td>table of points y coordinates values<br><code>table key</code> (number, zero based) -  point number<br><code>table value</code> (signed number) - point's y coordonate value </td></tr><tr><td><code>x</code></td><td>table</td><td>table of points x coordinates values<br><code>table key</code> (number, zero based) -  point number<br><code>table value</code> (signed number) - point's x coordonate value </td></tr></tbody></table>

## API Status

<table><thead><tr><th width="161"></th><th width="71.1764705882353" data-type="checkbox">Avail</th><th width="145" data-type="select">Status</th><th>Comment</th></tr></thead><tbody><tr><td>BW radios</td><td>true</td><td></td><td></td></tr><tr><td>Color radios</td><td>true</td><td></td><td></td></tr></tbody></table>

## Change log

<table><thead><tr><th width="177">EdgeTX version</th><th>Change</th></tr></thead><tbody><tr><td>2.4.0</td><td>Introduced</td></tr><tr><td>2.9.0 </td><td>changed curveID index from zero based to normal LUA (starts from 1)</td></tr></tbody></table>

## Examples

Example description

```lua
-- sample script
```
