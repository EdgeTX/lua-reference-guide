# lcd.drawScreenTitle

`lcd.drawScreenTitle(title, page, pages)`

Draw a title bar

## Parameters

| Name | Req | Type | Description |
| --- | --- | --- | --- |
| `title` | yes | `string` | text for the title |
| `page` | yes | `integer` | page number |
| `pages` | yes | `integer` | total number of pages. Only used as indicator on the right side of title bar. (i.e. idx=2, cnt=5, display `2/5`) |

## Returns

None.

## Availability

- Since: `2.0.0`
- Radio support: `bw-lcd`

## Notes

- Only available on Taranis

## Source

`radio/src/lua/api_stdlcd.cpp`
