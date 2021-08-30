---
description: >-
  Lua is a small but powerful language. This section will explain a few of the
  most important concepts.
---

# Lua Basics

## Introduction

Lua was chosen for OpenTX, and hence also EdgeTX, because it is a small language designed to be highly extensible by libraries written in C and C++, and hence integrate into other systems like our radios. It is also relatively efficient, both in terms of memory and CPU usage, and hence well suited for the radios.

In addition to the provided libraries, Lua has a very elegant mechanism for loading new Lua code modules during run-time. A lot of the elegance comes from the way that the loading mechanism meshes with another concept supported by Lua: first class functions with closures.

## First Class Functions

Computer science pioneer Christopher Strachey introduced the concept of functions as _first-class objects_ in his paper F[undamental Concepts in Programming Languages](https://web.archive.org/web/20100216060948/http://www.cs.cmu.edu/~crary/819-f09/Strachey67.pdf) from 1967. What it means is simply that functions can be treated as other variables: as arguments passed in function calls, as results returned from function calls, and a function identifier can be re-assigned to another block of function code.

In Lua, this means that a function declaration is really "syntactic sugar" for assigning a variable to the chunk of code that is called when the function is invoked, i.e.

`local function f(x) return x + 1 end`

is the same as 

`local f = function(x) return x + 1 end`

You can even add functions to Lua tables, i.e. 

`t = { f = f }`

will add the above function to the table `t`, as a field that is also called `f`. Does that look familiar to the return statement required at the end of a Lua script? 

Yes indeed, because a script is really an anonymous function that returns a list of functions to the system. The function declarations assign variables to chunks of function code, these variables are added to the list returned at the end of the script, and the system then calls the functions periodically to run the script.

## Closures

Another important concept that goes with first-class functions, is _closures_. This is the environment of the function with the variable names that the function can see. Please consider the following function `counter` that returns another function:

```text
local function counter(start, step)
  local x = start
  
  return function()
    local y = x
    x = x + step
    return y
  end
end
```

The function is returned directly without being assigned to a variable name. The _closure_ of the function returned is the body of the function `counter`, containing both the arguments `start` and `step`, and the local variable `x`. So if `c1 = counter(1, 1)` then `c1()` will return 1, 2, 3, ... and if `c2 = counter(2, 3)` then `c2()` will return 2, 5, 8, ...

Likewise, the local variables that you declare outside the functions of your script can be used by all of the functions in your script, they persist between function calls, but they are not visible to other scripts.

The [widget scripts](../part_i_-_script_type_overview/widget_scripts.md) are a little trickier, as you can register multiple instances of the same widget script, and all of these instances run within the same Lua closure. Therefore, local variables declared outside any functions in a widget script are shared among all of the widget script instances. But each call to the `create(...)` function returns a new `widget` list to the system. And since this list is unique to each instance, you can add private instance variables to it.

## References

The following two references are very helpful, both if you want to learn more about Lua, and if you want to search for answers to specific questions.

1. [Programming in Lua](https://www.lua.org/pil/)
2. [Lua 5.2 Reference Manual](https://www.lua.org/manual/5.2/manual.html)

