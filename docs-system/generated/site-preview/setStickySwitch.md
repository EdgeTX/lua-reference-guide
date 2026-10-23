# setStickySwitch

`setStickySwitch(id, value)`



## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `id` | yes | `integer` | identifying the sticky logical switch (zero for LS1 etc.). |
| `value` | yes | `true/false` | . The new value of the sticky logical switch. |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `bufferFull` | `true/false` | . This function sends a message from Lua to the logical switch processor via a buffer with eight slots that are read 10 times per second. If the buffer is full, then a true value is returned and no messages was sent (i.e. the switch was not changed). |

## Availability

- Since: `2.6`
- Radio support: `all`

## Source

`radio/src/lua/api_general.cpp`
