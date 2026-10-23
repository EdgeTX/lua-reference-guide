# playDuration

`playDuration(duration [, hourFormat [, volume]])`

Play a time value (text to speech)

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `duration` | yes | `integer` | number of seconds to play. Only integral part is used. |
| `hourFormat` | no | `integer` | : * `0 or not present` play format: minutes and seconds.  * `!= 0` play format: hours, minutes and seconds.  * @param volume (number):  - (1..5) override radio settings Wav volume for the duration of file  - omitting the parameter uses radio settings Wav volume |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `none` | `unknown` |  |

## Availability

- Since: `2.1.0`
- Radio support: `all`

## Source

`radio/src/lua/api_general.cpp`
