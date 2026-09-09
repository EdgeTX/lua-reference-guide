# serialRead

`serialRead([num])`



## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `num` | no | `integer` | : maximum number of bytes to read. If non-zero, serialRead will read up to num characters from the buffer.                        If 0 or left out, serialRead will read up to and including the first newline character or the end of the buffer.                        Note that the returned string may not end in a newline if this character is not present in the buffer. |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `str` | `unknown` | string. Empty if no new characters were available. |

## Availability

- Since: `2.3.8`
- Radio support: `all`

## Source

`radio/src/lua/api_general.cpp`
