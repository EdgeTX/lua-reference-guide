# getGeneralSettings

`getGeneralSettings()`

Returns (some of) the general radio settings

## Parameters

None.

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `-` | `table` | with elements: * `battWarn` (number) radio battery range - warning value  * `battMin` (number) radio battery range - minimum value  * `battMax` (number) radio battery range - maximum value  * `imperial` (number) set to a value different from 0 if the radio is set to the  IMPERIAL units  * `language` (string) radio language (used for menus)  * `voice` (string) voice language (used for speech)  * `gtimer` (number) radio global timer in seconds (does not include current session) |

## Availability

- Since: `2.0.6`
- Radio support: `all`

## Source

`radio/src/lua/api_general.cpp`
