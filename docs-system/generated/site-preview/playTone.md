# playTone

`playTone(frequency, duration, pause [, flags [, freqIncr [, volume]]])`

Play a tone

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `frequency` | yes | `integer` | tone frequency in Hz (from 150 to 15000) |
| `duration` | yes | `integer` | length of the tone in milliseconds |
| `pause` | yes | `integer` | length of the silence after the tone in milliseconds |
| `flags` | no | `integer` | : * `0 or not present` play with normal priority.  * `PLAY_BACKGROUND` play in background (built in vario function uses this context)  * `PLAY_NOW` play immediately |
| `freqIncr` | no | `integer` | positive number increases the tone pitch (frequency with time), negative number decreases it. The frequency changes every 10 milliseconds, the change is `freqIncr * 10Hz`. The valid range is from -127 to 127. |
| `volume` | no | `integer` | : - (1..5) override radio settings Beep volume for the duration of file  - omitting the parameter uses radio settings Beep volume |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `none` | `unknown` |  |

## Availability

- Since: `2.1.0`
- Radio support: `all`

## Source

`radio/src/lua/api_general.cpp`
