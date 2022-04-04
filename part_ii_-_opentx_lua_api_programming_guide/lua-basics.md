---
description: >-
  Lua is a small but powerful language. This section will explain a few of the
  most important concepts.
---

# Lua Basics

## Introduction

Lua was chosen for OpenTX, and hence also EdgeTX, because it is a small language designed to be highly extensible by libraries written in C and C++, so it can be integrated into other systems like EdgeTX. It is also relatively efficient, both in terms of memory and CPU usage, and hence well suited for the radios.

In addition to the provided libraries, Lua has a very elegant mechanism for loading new Lua code modules during run-time. A lot of the elegance comes from the way that the loading mechanism meshes with another concept supported by Lua: first class functions with closures.

## First Class Functions

Computer science pioneer Christopher Strachey introduced the concept of functions as _first-class objects_ in his paper [Fundamental Concepts in Programming Languages](https://web.archive.org/web/20100216060948/http://www.cs.cmu.edu/\~crary/819-f09/Strachey67.pdf) from 1967. What it means is that functions can be treated as other variables: as arguments passed in function calls, as results returned from function calls, and a function identifier can be re-assigned to another chunk of function code, just like a variable ca be assigned to a new value.

In Lua, a function declaration is really "syntactic sugar" for assigning a variable to the chunk of code that is called when the function is invoked, i.e.

`local function f(x) return x + 1 end`

is the same as

`local f = function(x) return x + 1 end`

You can even add functions to Lua tables, i.e.

`t = { f = f }`

will add the above function to the table `t`, as a field that is also called `f`. Does that look familiar to the return statement required at the end of a Lua script?

Yes indeed, because a script is really an anonymous function that returns a list of functions to the system. The function declarations assign variables to chunks of function code, these variables are added to the list returned at the end of the script, and the system then calls the functions periodically to run the script. So the script itself is run one time initially, and subsequently the functions returned by the last statement are called periodically.

## Closures

Another important concept that goes with first-class functions, is _closures_. This is the environment of the function with the variable names that the function can see. Please consider the following function `counter` that returns another function:

```lua
local function counter(start, step)
  local x = start

  return function()
    local y = x
    x = x + step
    return y
  end
end
```

The function is returned directly without being assigned to a variable name. The _closure_ of the function returned is the body of the function `counter`, containing both the arguments `start` and `step`, and the local variable `x`. So if `c1 = counter(1, 1)` then `c1()` will return 1, 2, 3, ... when called repeatedly, and if `c2 = counter(2, 3)` then `c2()` will return 2, 5, 8, ...

Likewise, the local variables that you declare outside the functions of your script can be used by all of the functions in your script, and they persist between function calls, but they are not visible to other scripts.

The [widget scripts](../part\_i\_-\_script\_type\_overview/widget\_scripts.md) are a little trickier, as you can register multiple instances of the same widget script, and all of these instances run within the same Lua closure. Therefore, local variables declared outside any functions in a widget script are shared among all of the instances of that script. But each call to the `create(...)` function returns a new `widget` list to the system. And since this list is unique to each instance, you can add private instance variables to it.

## Functions with Variable Number of Arguments

Please consider this function:

```
local function match(x, ...)
  for i, y in ipairs({...}) do
    if x == y then
      return true
    end
  end
  return false
end
```

It takes an argument `x` and a [vararg](https://www.lua.org/manual/5.2/manual.html#3.4.10) list `...` A vararg list is just like a list of arguments separated by commas, and you can call the function with any number of arguments greater than 1. Inside the function, you can also treat `...` like a comma separated list of variables, e.g. in the above function, `...` is converted to a table by `{...}` just like you could construct a table by e.g. `{a, b, c}`. The table is iterated with the `ipairs` function to look for an element matching the first argument `x`. So e.g. the following statement

`if event == EVT_VIRTUAL_ENTER or event == EVT_VIRTUAL_EXIT then`

can be replaced by

`if match(event, EVT_VIRTUAL_ENTER, EVT_VIRTUAL_EXIT) then`

You can also use `...` directly as a comma separated list of values, e.g. `local a, b, c = ...` will assign the three variables to the three first arguments following `x`, or `nil` if none are given.

## References

The [Lua 5.2 Reference Manual](https://www.lua.org/manual/5.2/manual.html) helpful, both if you want to learn more about Lua, and if you want to search for answers to specific questions.
