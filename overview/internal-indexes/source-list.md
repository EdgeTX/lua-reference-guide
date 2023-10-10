# Source List

EdgeTX internal Source List contains every source available on particular radio model.

## Source List groups

<table><thead><tr><th width="182.33333333333331">Group</th><th width="146">Name scheme</th><th>Description</th></tr></thead><tbody><tr><td>Inputs</td><td>I[01-32]</td><td>Input value</td></tr><tr><td>Mixes Scripts</td><td>LUA[1-7][a-f]</td><td>Mixes (custom) scripts value</td></tr><tr><td>Sticks</td><td>Rud,Ele,Thr,Ail</td><td>Stick position value</td></tr><tr><td>Potentiometers</td><td>S[1-x]</td><td>Potentiometer value</td></tr><tr><td>Sliders</td><td>LS,RS</td><td>Left or right slider value</td></tr><tr><td>Cyclic</td><td>CYC[1-3]</td><td>Cyclic (heli) value</td></tr><tr><td>Trims</td><td>T[1-x]</td><td>Trim switch value</td></tr><tr><td>Switches</td><td>S[A-J]</td><td>Physical switch value</td></tr><tr><td>Logical Switches</td><td>L[01-64]</td><td>Logical switch value</td></tr><tr><td>Trainer input</td><td>TR[1-16]</td><td>Trainer input value</td></tr><tr><td>Mixer channel</td><td>CH[01-32]</td><td>Mixer channel value</td></tr><tr><td>Global variables</td><td>GV[1-9]</td><td>Global variable value</td></tr><tr><td>Radio data</td><td>Batt</td><td>Radio battery level</td></tr><tr><td>Radio data</td><td>Time</td><td>Radio time</td></tr><tr><td>Radio data</td><td>GPS</td><td>Radio internal GPS data</td></tr><tr><td>Timers</td><td>Tmr[1-3]</td><td>Value of timer</td></tr><tr><td>Telemetry</td><td>Tele[1-64]</td><td>Current value of telemetry sensor</td></tr><tr><td>Telemetry</td><td>Tele[1-64]+</td><td>Maximum value of telemetry sensor</td></tr><tr><td>Telemetry</td><td>Tele[1-64]-</td><td>Minimum value of telemetry sensor</td></tr></tbody></table>

## Source List ID

{% hint style="info" %}
To avoid confusion wherever there is reference to Source List ID short-name **srcListID** is used.
{% endhint %}

Particular Source List ID is a integer number from 1 to whatever last source entry is used by EdgeTX developers during firmware implementation. Different Radios have different number of physical inputs that affects this list. Therefore for the same source type (ie LS04 - Logical switch number 4) **srcListID** can have different value on particular radio model

## Source List Name

{% hint style="info" %}
To avoid confusion wherever there is reference to Source List Name short-name **srcListName** is used.
{% endhint %}

Source List name can also change due to firmware changes during development or user configuration (ie. assigning custom name to input). In current version of EdgeTX firmware Source List Name also may contain special visual symbols to indicate type source (see [Special Charactes Constants](../../lua-api-reference/constants/special-character-constants.md)). \
&#x20;  &#x20;
