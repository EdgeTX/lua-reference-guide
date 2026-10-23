# getSourceIndex(sourceName)

#### Parameters

* `sourceName`: string naming a value source as it is shown on radio menus where you can select it. Notice that many names have [special characters](../constants/special-character-constants.md) in them.

Return value

* `sourceIndex`: integer. The source index, which can be used as input for `getSourceName(sourceIndex)`, `getValue(sourceIndex)`, and `getFieldInfo(sourceIndex)`.

#### Notice

The source names shown on the screen are not the same as the names used by `getFieldInfo` and `getValue`. But the indices are the same, so e.g. `getValue(index)` will work with the indices obtained here.

This function is rather time consuming, and should not be used repeatedly in a script, if it can be avoided.

#### Status

Current Introduced in 2.6
