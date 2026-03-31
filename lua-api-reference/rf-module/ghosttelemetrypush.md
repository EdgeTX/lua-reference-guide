---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/Ly8RKETivxoHMb7Zzqkb/lua-api-reference/rf-module/ghosttelemetrypush
---

# ghostTelemetryPush()

This functions allows for sending telemetry data toward the Ghost link.

When called without parameters, it will only return the status of the output buffer without sending anything.

@status current Introduced in 2.7.0

**Parameters**

* `command` command
* `data` table of data bytes

**Return value**

* `boolean` data queued in output buffer or not.
* `nil` incorrect telemetry protocol.
