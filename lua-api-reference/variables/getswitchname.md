---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/Ly8RKETivxoHMb7Zzqkb/lua-api-reference/variables/getswitchname
---

# getSwitchName(switchIndex)

@status current Introduced in 2.6

## Parameter

* `switchIndex`: integer identifying a switch as returned by `getSwitchIndex(positionName)` or fields in the table returned by `model.getLogicalSwitch(switch)` identifying switches.

## Return value

* value: string naming the switch position as it is shown on radio menus where a switch can be chosen.
