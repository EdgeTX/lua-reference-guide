# getVersion

`getVersion()`

Return OpenTX version

## Parameters

None.

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `-` | `string` | OpenTX version (ie "2.1.5") |
| `opentx_version_ie_2` | `string` | OpenTX version (ie "2.1.5") |
| `radio_type_x12s_x10_x9e_x9d_x9d_or_x7` | `string` | radio type: `x12s`, `x10`, `x9e`, `x9d+`, `x9d` or `x7`. |
| `major_version_ie_2_if_version_2` | `integer` | major version (ie 2 if version 2.1.5) |
| `minor_version_ie_1_if_version_2` | `integer` | minor version (ie 1 if version 2.1.5) |
| `revision_number_ie_5_if_version_2` | `integer` | revision number (ie 5 if version 2.1.5) |
| `os_name_i` | `string` | OS name (i.e. EdgeTX or nil if OpenTX) |

## Availability

- Since: `2.0.0`
- Radio support: `all`

## Source

`radio/src/lua/api_general.cpp`
