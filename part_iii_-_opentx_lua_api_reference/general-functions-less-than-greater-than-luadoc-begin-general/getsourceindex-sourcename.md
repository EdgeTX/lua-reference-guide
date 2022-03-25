# getSourceIndex(sourceName)

#### Parameters

* `sourceName`: string naming a value source as it is shown on radio menus where you can select it. Notice that many names have[ special characters](broken-reference) in them.&#x20;

Return value

* `sourceIndex`: integer. The source index, which can be used as input for `getSourceName(sourceIndex)`, `getValue(sourceIndex)`, and `getFieldInfo(sourceIndex)`.&#x20;

#### Notice

The source names shown on the screen are not the same as the names used by `getFieldInfo` and `getValue`. But the indices are the same, so e.g. `getValue(index)` will work with the indices obtained here.&#x20;

This function is rather time consuming, and should not be used repeatedly in a script, if it can be avoided.

#### Status

Current Introduced in 2.6\
