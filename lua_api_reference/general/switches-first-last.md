# switches(\[first\[, last]])

This is an iterator function over switch positions.&#x20;

`for switchIndex, switchName in switches() do ...`&#x20;

will iterate over all available switch positions.

### Parameters

* `first`: the first switch index. If `nil` or omitted, the first available switch is used.
* `last`: the last switch index. If `nil` or omitted, the last available switch is used.

### Status

Current Introduced in 2.6
