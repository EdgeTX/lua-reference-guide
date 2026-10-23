# setTelemetryValue

`setTelemetryValue(id, subID, instance, value [, unit [, precision [, name]]])`



## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `id` | yes | `unknown` | Id of the sensor, valid range is from 0 to 0xFFFF |
| `subID` | yes | `unknown` | subID of the sensor, usually 0, valid range is from 0 to 7 |
| `instance` | yes | `unknown` | instance of the sensor (SensorID), valid range is from 0 to 0xFF |
| `value` | yes | `unknown` | fed to the sensor |
| `unit` | no | `unknown` | unit of the sensor [Full list](../../appendix/units.html) |
| `precision` | no | `unknown` | the precision of the sensor * `0 or not present` no decimal precision.  * `!= 0` value is divided by 10^precision, e.g. value=1000, prec=2 => 10.00. |
| `name` | no | `string` | Name of the sensor if it does not yet exist (4 chars). * `not present` Name defaults to the Id.  * `present` Sensor takes name of the argument. Argument must have name surrounded by quotes: e.g., "Name" |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `true,` | `unknown` | if the sensor was just added. In this case the value is ignored (subsequent call will set the value) |

## Availability

- Since: `2.2.0`
- Radio support: `all`

## Notes

- All three parameters `id`, `subID` and `instance` can't be zero at the same time. At least one of them
must be different from zero.

## Source

`radio/src/lua/api_general.cpp`
