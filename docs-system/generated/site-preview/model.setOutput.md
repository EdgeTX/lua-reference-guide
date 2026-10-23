# model.setOutput

`model.setOutput(index, value)`

Set servo parameters

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `index` | yes | `integer` | channel number (use 0 for CH1) |
| `value` | yes | `table` | servo parameters, see model.getOutput() for table format |

## Returns

None.

## Availability

- Since: `2.0.0`
- Radio support: `all`

## Notes

- If a parameter is missing from the value, then
that parameter remains unchanged.

## Source

`radio/src/lua/api_model.cpp`
