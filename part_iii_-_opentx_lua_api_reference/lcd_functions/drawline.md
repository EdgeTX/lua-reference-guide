# lcd.drawLine\(x1, y1, x2, y2, pattern, flags\)

Draw a straight line on LCD

@status current Introduced in 2.0.0

### Parameters

* `x1,y1` \(positive numbers\) starting coordinate
* `x2,y2` \(positive numbers\) end coordinate
* `pattern` TODO
* `flags` TODO

### Return value

none

#### Notice

If the start or the end of the line is outside the LCD dimensions, then the whole line will not be drawn \(starting from OpenTX 2.1.5\)

## Examples

[lcd/drawLine-example](https://raw.githubusercontent.com/opentx/lua-reference-guide/opentx_2.2/lcd/drawLine-example.lua)

```lua
local alpha = (2 * math.pi) / 10

local function getPoint(centerX, centerY, radius, point)
  local omega = alpha * point
  local r = radius*(point % 2 + 1)/2
  local X = (r * math.sin(omega)) + centerX
  local Y = (r * math.cos(omega)) + centerY
  return X, Y
end

local function drawStar(centerX, centerY, radius, pattern, flags)
  local point = 10
  local startX, startY = getPoint(centerX, centerY, radius, point)
  for point = 1, 10 do
    local nextX, nextY = getPoint(centerX, centerY, radius, point)
    lcd.drawLine(startX, startY, nextX, nextY, pattern, flags)
    startX = nextX
    startY = nextY
  end
end

local function run(event)
  lcd.clear()
  lcd.drawText(1,1,"drawLine() example", 0)
  drawStar(30, 35, 25, SOLID, FORCE)
  drawStar(30, 35, 20, DOTTED, FORCE)
  drawStar(30, 35, 15, SOLID, FORCE)
end

return{run=run}
```

![](../../.gitbook/assets/drawLine-example%20%281%29.png)

