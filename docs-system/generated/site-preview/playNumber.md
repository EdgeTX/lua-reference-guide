# playNumber

`playNumber(value, unit [, attributes [, volume]])`

Play a numerical value (text to speech)

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `value` | yes | `integer` | number to play. Value is interpreted as integer. |
| `unit` | yes | `integer` | unit identifier [Full list]((../appendix/units.html)) |
| `attributes` | no | `integer` | possible values: * `0 or not present` plays integral part of the number (for a number 123 it plays 123)  * `PREC1` plays a number with one decimal place (for a number 123 it plays 12.3)  * `PREC2` plays a number with two decimal places (for a number 123 it plays 1.23) |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `none` | `unknown` |  |

## Availability

- Since: `2.0.0`
- Radio support: `all`

## Source

`radio/src/lua/api_general.cpp`
