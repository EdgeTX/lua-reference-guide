# del(file or directory)

@status current Introduced in 2.9.0

## Example

```lua
  if del("/SCRIPTS/TOOLS/deleteme.txt") == 0 then
     -- successfully deleted file
  else
     -- failed to delete file
  end
```

### Parameters

Path to file or directory to be deleted

### Return value

Returns FRESULT (e.g. 0=OK, 4=File not found, 5=Path not found, 6=Path invalid)
