# LUA version and included libraries

## LUA Version

EdgeTX 2.10 uses LUA interpreter and compiler version 5.2\
For detailed reference read [Lua 5.2 Reference Manual](https://www.lua.org/manual/5.2/manual.html)

## Included standard libraries

| Lua Standard Libraries                                   | Comment                                                              |
| -------------------------------------------------------- | -------------------------------------------------------------------- |
| [math](https://www.lua.org/manual/5.2/manual.html#6.6)   | <mark style="color:green;">included</mark>                           |
| [string](https://www.lua.org/manual/5.2/manual.html#6.4) | <mark style="color:green;">included</mark>                           |
| [bit32](https://www.lua.org/manual/5.2/manual.html#6.7)  | <mark style="color:green;">included</mark>                           |
| [table](https://www.lua.org/manual/5.2/manual.html#6.5)  | <mark style="color:yellow;">included only on color LCD Radios</mark> |
| [io](io-library.md)                                      | <mark style="color:yellow;">included partialy</mark>                 |
| package                                                  | <mark style="color:red;">not included</mark>                         |
| coroutine                                                | <mark style="color:red;">not included</mark>                         |
| os                                                       | <mark style="color:red;">not included</mark>                         |
| debug                                                    | <mark style="color:red;">not included</mark>                         |
