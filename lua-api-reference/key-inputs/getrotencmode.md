---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/Ly8RKETivxoHMb7Zzqkb/lua-api-reference/key-inputs/getrotencmode
---

# getRotEncMode()

Return rotary encoder mode

@status current Introduced in 2.8.0

**Parameters**

none

**Return value**

* `number` in list: Normal = 0, Both V and H inverted = 1, V-N = 2, V-A = 3
* `return 0` on radio without rotary encoder
