# popupConfirmation

`popupConfirmation(title, event)`

Raises a pop-up on screen that asks for confirmation

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `title` | yes | `string` | title to display |
| `message` | yes | `string` | text to display |
| `event` | yes | `integer` | the event variable that is passed in from the Run function (key pressed) |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `"CANCEL"` | `unknown` | user pushed EXIT key |

## Availability

- Since: `2.2.0`
- Radio support: `all`

## Notes

- Use only from stand-alone and telemetry scripts.

## Source

`radio/src/lua/api_general.cpp`
