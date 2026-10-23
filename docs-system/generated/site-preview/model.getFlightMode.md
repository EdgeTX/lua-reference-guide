# model.getFlightMode

`model.getFlightMode(index)`



## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `index` | yes | `integer` | flight mode number (use 0 for FM0) |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `-` | `nil` | requested input or line does not exist |
| `-` | `table` | input data: * `name` (string) input line name  * `switch` (number) input switch index  * `fadeIn` (number) fade in value (in 0.1s)  * `fadeOut` (number) fade out value (in 0.1s)  * `trimsValues` (table) table of trim values:    * `key` is trim number (zero based)    * `value` is trim value  * `trimsModes` (table) table of trim mode:    * `key` is trim number (zero based)    * `value` is trim mode |

## Availability

- Since: `2.3.10`
- Radio support: `all`

## Source

`radio/src/lua/api_model.cpp`
