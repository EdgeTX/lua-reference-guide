# Lua version

## Included libraries

Up to version 2.10, EdgeTX uses Lua 5.2 (interpreter and compiler). From version 2.11 onward, it uses Lua 5.3. For the full language reference, see the [Lua 5.2 Reference Manual](https://www.lua.org/manual/5.2/manual.html) or the [Lua 5.3 Reference Manual](https://www.lua.org/manual/5.3/manual.html).

!!! warning
    Binary files `*.luac` compiled with Lua 5.2 are not compatible with the Lua 5.3 interpreter. If you distribute binary files, they must be recompiled.

## Included standard libraries

| Lua Standard Library                                      | Support                                |
| ----------------------------------------------------------- | --------------------------------------- |
| [math](https://www.lua.org/manual/5.2/manual.html#6.6)    | **Included**                           |
| [string](https://www.lua.org/manual/5.2/manual.html#6.4)  | **Included**                           |
| [bit32](https://www.lua.org/manual/5.2/manual.html#6.7)   | **Included**                           |
| [table](https://www.lua.org/manual/5.2/manual.html#6.5)   | **Included on color LCD radios only**  |
| [io](io-library.md)                                        | **Partially included**                 |
| package                                                    | Not included                           |
| coroutine                                                  | Not included                           |
| os                                                         | Not included                           |
| debug                                                      | Not included                           |
