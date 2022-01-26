# setStickySwitch(id, value)

Sets the value of a sticky logical switch.

@status current Introduced in 2.6

## Parameters

* id: integer identifying the sticky logical switch (zero for LS1 etc.).
* value: true/false. The new value of the sticky logical switch.

## Return value

*   bufferFull: true/false. This function sends a message from Lua to the logical switch processor via a buffer with eight slots that are read 10 times per second. If the buffer is full, then a true value is returned, and no message was sent (i.e. the switch was not changed).

