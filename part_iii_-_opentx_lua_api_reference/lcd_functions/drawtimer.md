# lcd.drawTimer\(x, y, value \[, flags\]\)

Display a value formatted as time at \(x,y\)

@status current Introduced in 2.0.0, `SHADOWED` introduced in 2.2.1

### Parameters

* `x,y` \(positive numbers\) starting coordinate
* `value` \(number\) time in seconds
* `flags` \(unsigned number\) drawing flags:
  * `0 or not specified` normal representation \(minutes and seconds\)
  * `TIMEHOUR` display hours
  * other general LCD flag also apply
  * `SHADOWED` Horus only, apply a shadow effect

### Return value

none

## Examples

[lcd/drawTimer-example](https://raw.githubusercontent.com/opentx/lua-reference-guide/opentx_2.2/lcd/drawTimer-example.lua)

```lua
local upTime

local function background()
  upTime = getTime() / 100
end

local function run(event)
  background()
  lcd.clear()
  lcd.drawText(1, 1,"drawTimer() example", 0)
  lcd.drawTimer(1, 10, upTime, TIMEHOUR)
end

return{run=run}
```

![](../../.gitbook/assets/drawTimer-example%20%281%29%20%281%29.png)

