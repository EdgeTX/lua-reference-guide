# model.setSwashRing

`model.setSwashRing(params)`

Set heli swash parameters

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `params` | yes | `table` | swash ring parameters, see model.getSwashRing() for table format |

## Returns

None.

## Availability

- Since: `2.8.0`
- Radio support: `all`

## Notes

- If a parameter is missing, then that parameter remains unchanged.

## Source

`radio/src/lua/api_model.cpp`
