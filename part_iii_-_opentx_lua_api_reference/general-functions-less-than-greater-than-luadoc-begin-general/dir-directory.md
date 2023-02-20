# dir(directory)

Return an iterator listing all the files and directories name in a directory

@status current Introduced in 2.5.0

## Example

```lua
  for fname in dir(".") do
    print(fname)
  end
```

### Parameters

* `directory` (string) Working directory

### Return value

none
