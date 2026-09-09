# getShmVar

`getShmVar(id)`



## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `id` | yes | `integer` | between 1 and 16 identifying the shared memory variable. |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `value` | `integer` | . The value of the shared memory variable. |

## Availability

- Since: `2.6`
- Radio support: `color-lcd`

## Notes

- Only available on radios with color display

## Source

`radio/src/lua/api_general.cpp`
