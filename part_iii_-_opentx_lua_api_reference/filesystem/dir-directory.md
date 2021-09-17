# dir\(directory\)

Return an iterator listing all the files and directories name in a directory

@status current Introduced in 2.5.0

**Parameters**

* `directory` \(string\) Working directory

**Return value**

none

#### Example

```lua
    local var y = 40
    for fname in dir("/SCRIPTS") do
        lcd.drawText(5,y, fname, TEXT_COLOR)
        y = y + 20
    end
```

