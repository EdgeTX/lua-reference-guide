---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/Ly8RKETivxoHMb7Zzqkb/lua-api-reference/variables/getswitchvalue
---

# getSwitchValue(switchIndex)

@status current Introduced in 2.6

## Parameter

* `switchIndex`: integer identifying a switch as returned by `getSwitchIndex(positionName)` or fields in the table returned by `model.getLogicalSwitch(switch)` identifying switches.

## Return value

* `value`: true/false. The value of the switch.
