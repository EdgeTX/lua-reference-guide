# serialGetPower(port\_nr)

@status current Introduced in 2.9.0

### Parameters

* `port_nr:` valid values are only 0 and 1 on radios that have SWSERIALPOWER defined&#x20;
  * 0 - first serial port, e.g. on TX16S AUX1&#x20;
  * 1 - second serial port, e.g. on TX16S AUX2

### Return value

* `value:` true for power enabled, false for power disabled.
* `nil` serial port power control not available
