# model.setCurve

`model.setCurve(curve, params)`

Set Curve parameters

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `curve` | yes | `integer` | curve number (use 0 for Curve1) |
| `params` | yes | `integer` | see model.getCurve return format for table format. setCurve uses standard lua array indexing and arrays start at index 1 |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `0` | `integer` | - Everything okay 1 - Wrong number of points          2 - Invalid Curve number          3 - Cuve does not fit anymore          4 - point of out of index          5 - x value not monotonically increasing          6 - y value not in range [-100;100]          7 - extra values for y are set          8 - extra values for x are set |

## Availability

- Since: `2.2.0`
- Radio support: `all`

## Source

`radio/src/lua/api_model.cpp`
