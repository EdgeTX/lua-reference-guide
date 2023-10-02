# model.getInfo()

Get current Model information

@status current Introduced in 2.0.6, changed in 2.2.0, filename added in 2.6.0, extendedLimits, jitterFilter, and labels added in 2.8.0

## Parameters

none

## Return value

* `table` model information:
  * `name` (string) model name
  * `extendedLimits` (boolean) extended limits enabled
  * `jitterFilter` (number) model level ADC filter
  * `bitmap` (string) bitmap name (not present on X7)
  * `filename` (string) model filename
