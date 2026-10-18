---
description: >-
  In addition to the key events described in the previous section, radios with a
  color touch screen also provide touch events to the widget scripts.
---

# Touch Event Constants

The following touch events are passed in the `event` argument to the widget script `refresh` function \(when in full screen mode\), just like the key events. The following touch events are provided:

| Touch event name | Description |
| :--- | :--- |
| `EVT_TOUCH_FIRST` | When the finger touches down on the screen |
| `EVT_TOUCH_TAP` | If the finger leaves the screen after a quick tap |
| `EVT_TOUCH_BREAK` | If the finger leaves the screen without tap or slide |
| `EVT_TOUCH_SLIDE` | Repeats while the finger is sliding on the screen |

In addition to the above touch events a `touchState` table is passed to `refresh` with the following addional data fields:

| `touchState` field | Description |
| :--- | :--- |
| `x`, `y` | Current touch point |
| `startX`, `startY` | Point where slide started |
| `slideX`, `slideY` | Movement since previous `EVT_TOUCH_SLIDE` event \(or start of slide\) |
| `swipeUp`, `swipeDown`, `swipeLeft`, `swipeRight` | The field is present and equal to `true` if a swipe event occurred in that direction |
| `tapCount` | Counts the number of consecutive taps |

## Notes:

* `touchState` is `nil` if `event` is not a touch event. This can be used to test if we have a touch event or a key event.
* Since Lua evaluates `nil` to `false` and everything else to `true`, `if touchState then` means we have a touch event.
* `x, y` are present for all touch events.
* `startX, startY, slideX, slideY` are only present with `EVT_TOUCH_SLIDE`.
* `swipeUp`, `swipeDown`, `swipeLeft`, `swipeRight` _may_ be present only with `EVT_TOUCH_SLIDE`.
* `tapCount` is zero for anything but `EVT_TOUCH_TAP`.
