# popupInput

`popupInput(title, event, input, min, max)`

Raises a pop-up on screen that allows uses input

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `title` | yes | `string` | text to display |
| `event` | yes | `integer` | the event variable that is passed in from the Run function (key pressed) |
| `input` | yes | `integer` | value that can be adjusted by the +/- keys |
| `min` | yes | `integer` | min value that input can reach (by pressing the - key) |
| `max` | yes | `integer` | max value that input can reach |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `-` | `integer` | result of the input adjustment |
| `"OK"` | `unknown` | user pushed ENT key |
| `"CANCEL"` | `unknown` | user pushed EXIT key |

## Availability

- Since: `2.0.0`
- Radio support: `all`

## Notes

- Use only from stand-alone and telemetry scripts.

## Source

`radio/src/lua/api_general.cpp`
