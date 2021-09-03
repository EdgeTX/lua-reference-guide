# fstat\(path\)

Checks the existence of file or directory.   
If not exist, return nil.   
If exist, return the object information.

@status current Introduced in 2.5.0

**Parameters**

* `path` \(string\) path to the object

**Return value**

* `table` object info, table elements:
* `size` \(number\) file size
* `attrib` \(number\) file attribute flags
* `time` \(table\) table with last time modified date and times, table elements:
  * `year` \(number\) year
  * `mon` \(number\) month
  * `day` \(number\) day of month
  * `hour` \(number\) hours
  * `hour12` \(number\) hours in US format
  * `min` \(number\) minutes
  * `sec` \(number\) seconds
  * `suffix` \(text\) am or pm

#### Example

```lua
  info = fstat("radio")
  if info ~= nil then
    if (info.attrib == AM_DIR) then
      print("is a directory")
    end

    size = info.size
    time = info.time
  end
```

