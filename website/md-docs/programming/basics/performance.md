# Performance

RC control always has priority over Lua execution.

Lua scripts receive only a limited share of execution time in each radio cycle. If a script uses too much of that assigned time, the system may terminate the Lua process.

Keep scripts responsive by:

- doing less work per call
- spreading heavy work across multiple cycles
- avoiding repeated expensive lookups
- testing performance on the real target radio
