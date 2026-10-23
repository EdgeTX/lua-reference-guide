# getRAS

`getRAS()`

Return the RAS value or nil if no valid hardware found

## Parameters

None.

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `-` | `integer` | representing RAS value. Value bellow 0x33 (51 decimal) are all ok, value above 0x33 indicate a hardware antenna issue. This is just a hardware pass/fail measure and does not represent the quality of the radio link |

## Availability

- Since: `2.2.0`
- Radio support: `all`

## Notes

- RAS was called SWR in the past

## Source

`radio/src/lua/api_general.cpp`
