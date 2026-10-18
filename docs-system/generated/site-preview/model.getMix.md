# model.getMix

`model.getMix(channel, line)`

Get configuration for specified Mix

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `channel` | yes | `integer` | channel number (use 0 for CH1) |
| `line` | yes | `integer` | mix number (use 0 for first line(mix)) |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `-` | `nil` | requested channel or line does not exist |
| `-` | `table` | mix data: * `name` (string) mix line name  * `source` (number) source index  * `weight` (number) weight value (-512 to 511) or source (>= 1024 or <= -1024)  * `offset` (number) offset value (-512 to 511) or source (>= 1024 or <= -1024)  * `switch` (number) switch index  * `multiplex` (number) multiplex (0 = ADD, 1 = MULTIPLY, 2 = REPLACE)  * `curveType` (number) curve type (function, expo, custom curve)  * `curveValue` (number) curve index  * `flightModes` (number) bit-mask of active flight modes  * `carryTrim` (boolean) carry trim  * `mixWarn` (number) warning (0 = off, 1 = 1 beep, .. 3 = 3 beeps)  * `delayPrec` precision of delay up/down (1 or 10)  * `delayUp` (number) delay up (time in 1/10 s)  * `delayDown` (number) delay down  * `speedPrec` precision of speed up/down (1 or 10)  * `speedUp` (number) speed up  * `speedDown` (number) speed down |

## Availability

- Since: `2.0.0`
- Radio support: `all`

## Source

`radio/src/lua/api_model.cpp`
