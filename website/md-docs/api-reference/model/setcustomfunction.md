# model.setCustomFunction(function, value)

Set Custom Function parameters

@status current Introduced in 2.0.0, TODO rename function

## Parameters

* `function` (unsigned number) custom function number, see [Special Function Constants](../constants/special-function-constants.md).
* `value` (table) custom function parameters, see model.getCustomFunction() for table format

## Return value

none

### Notice

If a parameter is missing from the value, then that parameter remains unchanged.
