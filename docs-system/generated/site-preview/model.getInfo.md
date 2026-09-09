# model.getInfo

`model.getInfo()`

Get current Model information

## Parameters

None.

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `-` | `table` | model information: * `name` (string) model name  * `extendedLimits` (boolean) extended limits enabled  * `jitterFilter` (number) model level ADC filter  * `bitmap` (string) bitmap name (not present on X7)  * `filename` (string) model filename |

## Availability

- Since: `2.0.6`
- Radio support: `all`

## Source

`radio/src/lua/api_model.cpp`
