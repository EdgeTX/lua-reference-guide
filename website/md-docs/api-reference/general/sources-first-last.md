# sources(\[first\[, last]])

This is an iterator function over value sources.&#x20;

`for sourceIndex, sourceName in sources() do ...`

will iterate over all available value sources.

### Parameters

* `first`: the first source index. If `nil` or omitted, the first available source is used.
* `last`: the last soure index. If `nil` or omitted, the last available source is used.

### Status

current Introduced in 2.6
