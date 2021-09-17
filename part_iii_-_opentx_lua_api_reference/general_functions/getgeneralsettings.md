# getGeneralSettings\(\)

Returns \(some of\) the general radio settings

@status current Introduced in 2.0.6, `imperial` added in TODO, `language` and `voice` added in 2.2.0, gtimer added in 2.2.2.

### Parameters

none

### Return value

* `table` with elements:
  * `battWarn` \(number\) radio battery range - warning value
  * `battMin` \(number\) radio battery range - minimum value
  * `battMax` \(number\) radio battery range - maximum value
  * `imperial` \(number\) set to a value different from 0 if the radio is set to the

    IMPERIAL units

  * `language` \(string\) radio language \(used for menus\)
  * `voice` \(string\) voice language \(used for speech\)
  * `gtimer` \(number\) radio global timer in seconds \(does not include current session\)

## Examples

[general/getGeneralSettings-example](https://raw.githubusercontent.com/opentx/lua-reference-guide/opentx_2.2/general/getGeneralSettings-example.lua)

```lua
local function run(e)
  local settings = getGeneralSettings()
  lcd.clear()
  lcd.drawText(1,1,"getGeneralSettings() example",0)
  lcd.drawText(1,11,"battMin: ", 0)
  lcd.drawText(lcd.getLastPos()+2,11,settings['battMin'],0)
  lcd.drawText(1,21,"battMax: ", 0)
  lcd.drawText(lcd.getLastPos()+2,21,settings['battMax'],0)
  lcd.drawText(1,31,"imperial: ", 0)
  lcd.drawText(lcd.getLastPos()+2,31,settings['imperial'],0)
end

return{run=run}
```

![](../../.gitbook/assets/getGeneralSettings-example%20%281%29%20%281%29.png)

