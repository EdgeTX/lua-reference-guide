# getSourceValue(source)

Returns the value of a source. Supersedes `getValue`.

The list of fixed sources:

| OpenTX Version | Radio                                                                                                                                                                                                                                                                                                                                |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 2.0            | [all](http://downloads-20.open-tx.org/firmware/lua\_fields.txt)                                                                                                                                                                                                                                                                      |
| 2.1            | [X9D and X9D+](http://downloads-21.open-tx.org/firmware/lua\_fields\_taranis.txt), [X9E](http://downloads-21.open-tx.org/firmware/lua\_fields\_taranis\_x9e.txt)                                                                                                                                                                     |
| 2.2            | [X9D and X9D+](http://downloads.open-tx.org/2.2/release/firmware/lua\_fields\_x9d.txt), [X9E](http://downloads.open-tx.org/2.2/release/firmware/lua\_fields\_x9e.txt), [Horus](http://downloads.open-tx.org/2.2/release/firmware/lua\_fields\_x12s.txt)                                                                              |
| 2.3            | [X9D and X9D+](http://downloads.open-tx.org/2.3/release/firmware/lua\_fields\_x9d.txt), [X9E](http://downloads.open-tx.org/2.3/release/firmware/lua\_fields\_x9e.txt), [X7](http://downloads.open-tx.org/2.3/release/firmware/lua\_fields\_x7.txt), [Horus](http://downloads.open-tx.org/2.3/release/firmware/lua\_fields\_x12s.txt) |

In OpenTX 2.1.x the telemetry sources no longer have a predefined name. To get a telemetry value simply use it's sensor name. For example:

* Altitude sensor has a name "Alt"
* to get the current altitude use the source "Alt"
* to get the minimum altitude use the source "Alt-", to get the maximum use "Alt+"

value is nil for non-existing sources. all non-allowed sensors while FAI MODE is active, or if a telemetry item value has never been received

value is a table for GPS position:

* `lat` (number) latitude, positive is North
* `lon` (number) longitude, positive is East
* `pilot-lat` (number) pilot latitude, positive is North
* `pilot-lon` (number) pilot longitude, positive is East

value is a table for date/time, see getDateTime()

value is a table for battery cells(except where no cells were detected in which case the returned value is 0):

* table has one item for each detected cell:
* key (number) cell number (1 to number of cells)
* value (number) current cell voltage

@status current Introduced in 2.8.0

### Parameters

* `source` can be an index (number) (which was obtained by `getFieldInfo` or `getSourceIndex`) or a name (string) of the source.

### Return value

* `value` current source value (number), or last known telemetry item value.
* `isCurrent` is true for telemetry sources that are within the "Sensor Lost" duration and telemetry is streaming . Always true for non-telemetry items.
* `isFresh` is true for telemetry sources which have been recently updated and telemetry is streaming. Always true for non-telemetry items.

#### Notice

Getting a value by its numerical identifier is much faster than by its name. While `Cels` sensor returns current values of all cells in a table, a `Cels+` or `Cels-` will return a single value - the maximum or minimum Cels value.
