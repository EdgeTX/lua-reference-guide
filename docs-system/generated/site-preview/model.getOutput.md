# model.getOutput

`model.getOutput(index)`

Get servo parameters

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `index` | yes | `integer` | output number (use 0 for CH1) |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `-` | `nil` | requested output does not exist |
| `-` | `table` | output parameters: * `name` (string) name  * `min` (number) Minimum % * 10  * `max` (number) Maximum % * 10  * `offset` (number) Subtrim * 10  * `ppmCenter` (number) offset from PPM Center. 0 = 1500  * `symetrical` (number) linear Subtrim 0 = Off, 1 = On  * `revert` (number) irection 0 = ­­­---, 1 = INV  * `curve`    * (number) Curve number (0 for Curve1)    * or `nil` if no curve set |

## Availability

- Since: `2.0.0`
- Radio support: `all`

## Source

`radio/src/lua/api_model.cpp`
