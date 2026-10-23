# fstat

`fstat(path)`

Checks the existence of file or directory.
 If not exist, return nil.
 If exist, return the object information.

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `path` | yes | `string` | path to the object |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `-` | `integer` | object info, table elements: * 'size' (number) file size * 'attrib' (number) file attribute flags * 'time' (table) table with last time modified date and times, table elements:   * `year` (number) year   * `mon` (number) month   * `day` (number) day of month   * `hour` (number) hours   * `hour12` (number) hours in US format   * `min` (number) minutes   * `sec` (number) seconds   * `suffix` (text) am or pm |

## Availability

- Since: `2.5.0`
- Radio support: `all`

## Source

`radio/src/lua/api_filesystem.cpp`
