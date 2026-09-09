# getOutputValue

`getOutputValue(outputIndex)`



## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `outputIndex` | yes | `integer` | identifying the output channel number 0 for CH1, up to MAX_OUTPUT_CHANNELS - 1. |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `-` | `integer` | current output value (number). Zero is returned for: * non-existing outputs |

## Availability

- Since: `2.8.0`
- Radio support: `all`

## Source

`radio/src/lua/api_general.cpp`
