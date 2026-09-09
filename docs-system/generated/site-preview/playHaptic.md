# playHaptic

`playHaptic(duration, pause [, flags])`

Generate haptic feedback

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `duration` | yes | `integer` | length of the haptic feedback in milliseconds |
| `pause` | yes | `integer` | length of the silence after haptic feedback in milliseconds |
| `flags` | no | `integer` | : * `0 or not present` play with normal priority  * `PLAY_NOW` play immediately |

## Returns

None.

## Availability

- Since: `2.2.0`
- Radio support: `all`

## Source

`radio/src/lua/api_general.cpp`
