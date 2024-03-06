# serialSetPower(port\_nr, value)

@status current Introduced in 2.9.0

### Parameters

* `port_nr:` valid values are only 0 and 1 on radios that have SWSERIALPOWER defined&#x20;
  * 0 - first serial port, e.g. on TX16S AUX1&#x20;
  * 1 - second serial port, e.g. on TX16S AUX2
* `value:`&#x20;
  * 0 - disable power&#x20;
  * 1 - enable power

### Return value

* `success:` true/false
