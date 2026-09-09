# resetGlobalTimer

`resetGlobalTimer([type])`

Resets the radio global timer to 0.

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `type` | no | `unknown` | : if set to 'all', throttle ,throttle percent and session timers are reset too if set to 'session', radio session timer is reset too                     if set to 'ttimer', radio throttle timer is reset too                     if set to  'tptimer', radio throttle percent timer is reset too |

## Returns

None.

## Availability

- Since: `2.2.2`
- Radio support: `all`

## Source

`radio/src/lua/api_general.cpp`
