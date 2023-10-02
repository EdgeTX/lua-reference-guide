# getSwitchIndex(positionName)

@status current Introduced in 2.6

## Parameters

* `positionName`: string naming a switch position as it is shown on radio menus where you can select a switch. Notice that many names have special characters in them like arrow up/down etc. (see [Special Character Constants](../constants/special-character-constants.md)).

## Return value

* value: integer. The switchIndex, which can be used as input for \`getSwitchName(switchIndex)\` and \`getSwitchValue(switchIndex)\`. Also corresponds to the fields in the table returned by \`model.getLogicalSwitch(switch)\` identifying switches.
