# getSourceValue

`getSourceValue(source)`

Returns the value of a source. Superseeds getValue.

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `source` | yes | `string` | can be an index (number) (which was obtained by `getFieldInfo` or `getSourceIndex`) or a name (string) of the source. |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `-` | `integer` | current source value (number), or last known telemetry item value. |
| `isCurrent` | `unknown` | is true for telemetry sources that are within the "Sensor Lost" duration and telemetry is streaming . Always true for non-telemetry items. |
| `isFresh` | `unknown` | is true for telemetry sources which have been recently updated and telemetry is streaming. Always true for non-telemetry items. |

## Availability

- Since: `2.0.0`
- Radio support: `all`

## Notes

- The list of fixed sources:

| OpenTX Version | Radio |
|----------------|-------|
| 2.0 | [all](http://downloads-20.open-tx.org/firmware/lua_fields.txt) |
| 2.1 | [X9D and X9D+](http://downloads-21.open-tx.org/firmware/lua_fields_taranis.txt), [X9E](http://downloads-21.open-tx.org/firmware/lua_fields_taranis_x9e.txt) |
| 2.2 | [X9D and X9D+](http://downloads.open-tx.org/2.2/release/firmware/lua_fields_x9d.txt), [X9E](http://downloads.open-tx.org/2.2/release/firmware/lua_fields_x9e.txt), [Horus](http://downloads.open-tx.org/2.2/release/firmware/lua_fields_x12s.txt) |
| 2.3 | [X9D and X9D+](http://downloads.open-tx.org/2.3/release/firmware/lua_fields_x9d.txt), [X9E](http://downloads.open-tx.org/2.3/release/firmware/lua_fields_x9e.txt), [X7](http://downloads.open-tx.org/2.3/release/firmware/lua_fields_x7.txt), [Horus](http://downloads.open-tx.org/2.3/release/firmware/lua_fields_x12s.txt) |

In OpenTX 2.1.x the telemetry sources no longer have a predefined name.
To get a telemetry value simply use it's sensor name. For example:
 * Altitude sensor has a name "Alt"
 * to get the current altitude use the source "Alt"
 * to get the minimum altitude use the source "Alt-", to get the maximum use "Alt+"
- Getting a value by its numerical identifier is much faster than by its name.
While `Cels` sensor returns current values of all cells in a table, a `Cels+` or
`Cels-` will return a single value - the maximum or minimum Cels value.

## Source

`radio/src/lua/api_general.cpp`
