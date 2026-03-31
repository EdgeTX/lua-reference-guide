---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/Ly8RKETivxoHMb7Zzqkb/lua-api-reference/audio-sound/playhaptic
---

# playHaptic(duration, pause \[, flags])

Generate haptic feedback

@status current Introduced in 2.2.0

## Parameters

* `duration` (number) length of the haptic feedback in milliseconds
* `pause` (number) length of the silence after haptic feedback in milliseconds
* `flags` (number):
  * `0 or not present` play with normal priority
  * `PLAY_NOW` play immediately

## Return value

none
