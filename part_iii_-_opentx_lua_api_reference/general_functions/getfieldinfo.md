# getFieldInfo\(name\)

Return detailed information about field \(source\)

The list of valid sources is available:

| OpenTX Version | Radio |
| :--- | :--- |
| 2.0 | [all](http://downloads-20.open-tx.org/firmware/lua_fields.txt) |
| 2.1 | [X9D and X9D+](http://downloads-21.open-tx.org/firmware/lua_fields_taranis.txt), [X9E](http://downloads-21.open-tx.org/firmware/lua_fields_taranis_x9e.txt) |
| 2.2 | [X9D and X9D+](http://downloads.open-tx.org/2.2/release/firmware/lua_fields_x9d.txt), [X9E](http://downloads.open-tx.org/2.2/release/firmware/lua_fields_x9e.txt), [Horus](http://downloads.open-tx.org/2.2/release/firmware/lua_fields_x12s.txt) |

@status current Introduced in 2.0.8, 'unit' field added in 2.2.0

### Parameters

* `name` \(string\) name of the field

### Return value

* `table` information about requested field, table elements:
  * `id`   \(number\) field identifier
  * `name` \(string\) field name
  * `desc` \(string\) field description
  * 'unit' \(number\) unit identifier [Full list](https://github.com/opentx/opentx-2-2-lua-reference-guide/tree/01046aea966efa3beb7efe1cfb50bddec497f0c1/appendix/units.html)
* `nil` the requested field was not found

## Examples

[general/getFieldInfo-example](https://raw.githubusercontent.com/opentx/lua-reference-guide/opentx_2.2/general/getFieldInfo-example.lua)

```lua
local function run(e)
  local fieldinfo = getFieldInfo('rs')
  lcd.clear()
  lcd.drawText(1,1,"getFieldInfo() example",0)
  if fieldinfo then 
    lcd.drawText(1,11,"id: ", 0)
    lcd.drawText(lcd.getLastPos()+2,11,fieldinfo['id'],0)
    lcd.drawText(1,21,"name: ", 0)
    lcd.drawText(lcd.getLastPos()+2,21,fieldinfo['name'],0)
    lcd.drawText(1,31,"desc: ", 0)
    lcd.drawText(lcd.getLastPos()+2,31,fieldinfo['desc'],0)
  else
    lcd.drawText(1,11,"Requested field not available!", 0)    
  end
end

return{run=run}
```

![](../../.gitbook/assets/getFieldInfo-example%20%281%29%20%281%29%20%281%29.png)

