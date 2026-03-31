---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/Ly8RKETivxoHMb7Zzqkb/lua-api-reference/time/getdatetime
---

# getDateTime()

Return current system date and time that is kept by the RTC unit

## Parameters

none

## Return value

* `table` current date and time, table elements:
  * `year` (number) year
  * `mon` (number) month
  * `day` (number) day of month
  * `hour` (number) hours
  * `hour12` (number) hours in US format
  * `min` (number) minutes
  * `sec` (number) seconds
  * `suffix` (text) am or pm
