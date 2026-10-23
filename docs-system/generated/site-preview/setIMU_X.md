# setIMU_X

`setIMU_X(offset, range)`



## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `offset` | yes | `integer` | , offset in angular degree. -1 to offset to current X position |
| `range` | yes | `integer` | , range in angular degree. 180° max.90 means min/max value will be reached at 45° from offset position |

## Returns

None.

## Availability

- Since: `3.0`
- Radio support: `all`

## Source

`radio/src/lua/api_general.cpp`
