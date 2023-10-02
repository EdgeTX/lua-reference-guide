# model.getSwashRing()

Get heli swash parameters

@status current Introduced in 2.8.0

**Parameters**

none

**Return value**

* `table` with heli swash parameters:
* `type` (number) 0=---, 1=120, 2=120X, 3=140, 4=90
* `value` (number) swash ring value (normally 0)
* 'collectiveSource' (number) source index
* 'aileronSource' (number) source index
* 'elevatorSource' (number) source index
* 'collectiveWeight'(value) -100 to 100
* 'aileronWeight' (value) -100 to 100
* 'elevatorWeight' (value) -100 to 100
