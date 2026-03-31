---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/Ly8RKETivxoHMb7Zzqkb/lua-api-reference/bitmap/getsize
---

# Bitmap.getSize(name)

Return width, height of a bitmap object

@status current Introduced in 2.2.0

### Parameters

* `bitmap` (pointer) point to a bitmap previously opened with Bitmap.open()

### Return value

* `multiple` returns 2 values:
* (number) width in pixels
* (number) height in pixels

#### Notice

Only available on Horus
