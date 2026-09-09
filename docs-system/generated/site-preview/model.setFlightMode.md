# model.setFlightMode

`model.setFlightMode(index, params)`

Set Flight mode parameters

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `index` | yes | `integer` | flight mode number (use 0 for FM0) |
| `params` | yes | `unknown` | see model.getFlightMode return format for table format. |

## Returns

None.

## Availability

- Since: `2.3.10`
- Radio support: `all`

## Source

`radio/src/lua/api_model.cpp`
