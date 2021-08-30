---
description: >-
  Lua is a small but powerful language. This section will explain a few of the
  most important concepts.
---

# Lua Basics

## Introduction

Lua was chosen for OpenTX, and hence also EdgeTX, because it is a small language designed to be highly extensible by libraries written in C and C++, and hence integrate into other systems like our radios. It is also relatively efficient, both in terms of memory and CPU usage, and hence well suited for the radios.

In addition to the provided libraries, Lua has a very elegant mechanism for loading new Lua code modules during run-time. A lot of the elegance comes from the way that the loading mechanism meshes with another concept supported by Lua: first class functions with closures.

## First Class Functions with Closures

Computer science pioneer Christopher Strachey introduced the concept of functions as _first-class objects_ in his paper F[undamental Concepts in Programming Languages](https://web.archive.org/web/20100216060948/http://www.cs.cmu.edu/~crary/819-f09/Strachey67.pdf) from 1967. What it means is simply that functions can be treated as other variables: as arguments passed in function calls, as results returned from function calls, and a function identifier can be re-assigned to another block of function code.

In Lua, this means that a function declaration is really "syntactic sugar" for assigning a variable to the chunk of code that is called when the function is invoked, i.e.

`local function f(x) return x + 1 end`

is the same as 

`local f = function(x) return x + 1 end`

You can even add functions to Lua tables, i.e. 

`t = { f = f }`

will add the above function to the table `t`, as a field that is also called `f`. Does that look familiar to the return statement that is required at the end of a Lua script? This is because a script is a chunk of code that is the body of an anonymous function, which is called and then returns a list of functions to EdgeTX, which can be called periodically to run the script.



## References

The following two references are very helpful, both if you want to learn more about Lua, and if you want to search for answers to specific questions.

1. [Programming in Lua](https://www.lua.org/pil/)
2. [Lua 5.2 Reference Manual](https://www.lua.org/manual/5.2/manual.html)

