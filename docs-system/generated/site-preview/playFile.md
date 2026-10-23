# playFile

`playFile(filename [, volume])`

Play a file from the SD card

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `filename` | yes | `string` | full path to wav file (i.e. "/SOUNDS/en/system/tada.wav") Introduced in 2.1.0: If you use a relative path, the current language is appended to the path (example: for English language: `/SOUNDS/en` is appended) |
| `volume` | no | `integer` | : - (1..5) override radio settings Wav volume for the duration of file  - omitting the parameter uses radio settings Wav volume |

## Returns

| Name | Type | Description |
| --- | --- | --- |
| `none` | `unknown` |  |

## Availability

- Since: `2.0.0`
- Radio support: `all`

## Source

`radio/src/lua/api_general.cpp`
