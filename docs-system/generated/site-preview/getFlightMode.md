# getFlightMode

`getFlightMode(mode)`

Return flight mode data.

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `mode` | yes | `integer` | flight mode number to return (0 - 8). If mode parameter is not specified (or contains invalid value), then the current flight mode data is returned. |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `current_flight_mode_number_0_8` | `integer` | (current) flight mode number (0 - 8) |
| `current_flight_mode_name` | `string` | (current) flight mode name |

## Availability

- Since: `2.1.7`
- Radio support: `all`

## Source

`radio/src/lua/api_general.cpp`
