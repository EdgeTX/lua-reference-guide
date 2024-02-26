# Source List

EdgeTX internal Source List contains every source available on particular radio model.

## Source List groups

<table><thead><tr><th width="231">sourceListName</th><th width="182.33333333333331">Type</th><th>Description</th></tr></thead><tbody><tr><td>I[01-32]</td><td>Inputs</td><td>Input value</td></tr><tr><td>LUA[1-7][a-f]</td><td>Mixes Scripts</td><td>Mixes (custom) scripts value</td></tr><tr><td>Rud,Ele,Thr,Ail</td><td>Sticks</td><td>Stick position value</td></tr><tr><td>S[1-x]</td><td>Potentiometers</td><td>Potentiometer value</td></tr><tr><td>LS,RS</td><td>Sliders</td><td>Left or right slider value</td></tr><tr><td>CYC[1-3]</td><td>Cyclic</td><td>Cyclic (heli) value</td></tr><tr><td>T[1-x]</td><td>Trims</td><td>Trim switch value</td></tr><tr><td>S[A-J]</td><td>Switches</td><td>Physical switch value</td></tr><tr><td>L[01-64]</td><td>Logical Switches</td><td>Logical switch value</td></tr><tr><td>TR[1-16]</td><td>Trainer input</td><td>Trainer input value</td></tr><tr><td>CH[01-32]</td><td>Mixer channel</td><td>Mixer channel value</td></tr><tr><td>GV[1-9]</td><td>Global variables</td><td>Global variable value</td></tr><tr><td>Batt</td><td>Radio data</td><td>Radio battery level</td></tr><tr><td>Time</td><td>Radio data</td><td>Radio time</td></tr><tr><td>GPS</td><td>Radio data</td><td>Radio internal GPS data</td></tr><tr><td>Tmr[1-3]</td><td>Timers</td><td>Value of timer</td></tr><tr><td>Tele[1-64]</td><td>Telemetry</td><td>Current value of telemetry sensor</td></tr><tr><td>Tele[1-64]+</td><td>Telemetry</td><td>Maximum value of telemetry sensor</td></tr><tr><td>Tele[1-64]-</td><td>Telemetry</td><td>Minimum value of telemetry sensor</td></tr></tbody></table>

## Source List ID

Particular Source List ID is a integer number from 1 to whatever last source entry is used by EdgeTX developers during firmware implementation. Different Radios have different number of physical inputs that affects this list. Therefore for the same source type (ie LS04 - Logical switch number 4) **sourceListID** can have different value on particular radio model

{% hint style="info" %}
To avoid confusion wherever there is reference to Source List ID short-name **sourceListID** is used.
{% endhint %}

## Source List Name

Source List name can also change due to firmware changes during development or user configuration (ie. assigning custom name to input). In current version of EdgeTX firmware Source List Name also may contain special visual symbols to indicate type source (see [Special Charactes Constants](../../lua-api-reference/constants/special-character-constants.md)). \
&#x20;  &#x20;

{% hint style="info" %}
To avoid confusion wherever there is reference to Source List Name short-name **sourceListName** is used.
{% endhint %}
