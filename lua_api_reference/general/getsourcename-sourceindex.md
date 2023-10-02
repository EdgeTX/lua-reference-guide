# getSourceName(sourceIndex)

#### Parameters

* `sourceIndex`: integer identifying a value source as returned by `getSourceIndex(sourceName)` or the `id` field in the table returned by `getFieldInfo`.&#x20;

#### Return value

* `sourceName`: string naming the value source as it is shown on radio menus where a source can be chosen.

#### Notice&#x20;

The source names shown on the screen are not the same as the names used by `getFieldInfo` and `getValue`. But the indices are the same, so e.g. `getValue(index)` will work with the indices used here.

#### Status

Current Introduced in 2.6
