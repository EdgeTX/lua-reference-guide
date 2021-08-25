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



## References

The following two references are very helpful, both if you want to learn more about Lua, and if you want to search for answers to specific questions.

1. [Programming in Lua](https://www.lua.org/pil/)
2. [Lua 5.2 Reference Manual](https://www.lua.org/manual/5.2/manual.html)

