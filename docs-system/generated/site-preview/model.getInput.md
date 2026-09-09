# model.getInput

`model.getInput(input, line)`

Return input data for given input and line number

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `input` | yes | `integer` | input number (use 0 for Input1) |
| `line` | yes | `integer` | input line (use 0 for first line) |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `-` | `nil` | requested input or line does not exist |
| `-` | `table` | input data: * `name` (string) input line name  * `inputName` (string) input input name  * `source` (number) input source index  * `scale` (number)  input scaling (for telemetry)  * `weight` (number) input weight  * `offset` (number) input offset  * `switch` (number) input switch index  * `curveType` (number) curve type (function, expo, custom curve)  * `curveValue` (number) curve index  * `carryTrim` deprecated, please use trimSource instead. WARNING: carryTrim was getting negative values (carryTrim = - trimSource)  * 'trimSource' (number) a positive number representing trim source  * 'side' (number) input side (positive, negative or all)  * 'flightModes' (number) bit-mask of active flight modes |

## Availability

- Since: `2.0.0`
- Radio support: `all`

## Source

`radio/src/lua/api_model.cpp`
