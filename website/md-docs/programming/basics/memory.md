# Memory

Lua memory is limited on radios, especially on lower-memory targets.

Desktop environments such as Companion or the simulator can make a script look fine even when the same script will hit out-of-memory problems on real hardware.

Keep memory usage under control by:

- loading only what you need
- avoiding large temporary tables
- reusing data where possible
- testing on the real target radio
