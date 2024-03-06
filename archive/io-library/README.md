# io Library

The **io** library has been simplified and only a subset of functions and their functionality is available. What follows is a complete reference of io functions that are available to EdgeTX scripts

## Available functions:

* io.open()
* io.close()
* io.read()
* io.write()
* io.seek()

## Examples

### Read the whole file

```lua
-- this is a stand-alone script

local function run(event)
  print("lua io.read test")         -- print() statements are visible in Debug output window
  local f = io.open("foo.bar", "r")
  while true do
    local data = io.read(f, 10)     -- read up to 10 characters (newline char also counts!)
    if #data == 0 then break end    -- we get zero length string back when we reach end of the file
    print("data: "..data)
    end
  io.close(f)
  return 1
end

return {  run=run }
```

### Append data to file

```lua
-- this is a stand-alone script

local function run(event)
  print("lua io.write test")
  local f = io.open("foo.bar", "a")        -- open file in append mode
  io.write(f, "first line\r\nsecond line\r\n")
  io.write(f, 4, "\r\n", 35.6778, "\r\n")  -- one can write multiple items at the same time
  local foo = -4.45
  io.write(f, foo, "\r\n")
  io.close(f)
  return 1    -- this will end the script execution
end

return { run=run }
```
