# ghostTelemetryPop()

Pops a received Ghost Telemetry packet from the queue.

@status current Introduced in 2.7.0

**Parameters**

none

**Return value**

* `nil` queue does not contain any (or enough) bytes to form a whole packet
* `multiple` returns 2 values:
* type (number)
* packet (table) data bytes
