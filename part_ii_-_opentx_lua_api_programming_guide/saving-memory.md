---
description: >-
  This chapter will show you some ways that large script projects can be fitted
  into the limited memory of our radios.
---

# Saving Memory

Regarding memory, the situation is a bit different for the radios with black/white or grey scale screens and telemetry scripts, and the radios with color screens and widget scripts. The telemetry script radios only have 128-192 KB RAM memory - that is _very_ small! The widget script radios have 8 MB RAM memory. But the way that widgets are designed means that _all_ widget scripts present on the SD card will be loaded into memory, whether or not they are actually used. Therefore, different strategies should be applied to save memory for the two different types of radios and scripts.

## Telemetry Script Radios

Radios with black/white or grey scale screens and telemetry scripts such as e.g. FrSky Taranis, Xlite, Jumper T12 and Radiomaster TX16 have extremely small RAM memories, and therefore it may be necessary to divide up your script into smaller loadable modules.



## Widget Script Radios

Radios with color screens and widget scripts such as e.g. FrSky Horus, Jumper T16 and Radiomaster TX16 have fairly large RAM memories, but since all widget scripts present on the SD card are always loaded into memory, they could run out if a large number of big widget scripts are present on the card - even if they are not being used by the selected model. Therefore, large widget scripts should be divided into a small main script and a large loadable part.



