# model.setModule

`model.setModule(index, value)`

Set RF module parameters

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `index` | yes | `integer` | module index (0 for internal, 1 for external) |
| `value` | yes | `unknown` | module parameters, see model.getModule() |

## Returns

None.

## Availability

- Since: `2.2.0`
- Radio support: `all`

## Notes

- If a parameter is missing from the value, then
that parameter remains unchanged.

## Source

`radio/src/lua/api_model.cpp`
