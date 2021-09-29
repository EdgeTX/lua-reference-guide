---
description: >-
  Many of the lcd functions accept parameters named flags and patterns. The
  names and their meanings are described below.
---

# Flags and Pattern Constants

## Flags

| Name | Description | Version | Notes |
| :--- | :--- | :--- | :--- |
| 0 | normal font, default precision for numeric |  |  |
| XXLSIZE | jumbo font | 2.0.6 |  |
| DBLSIZE | double size font |  |  |
| MIDSIZE | mid sized font |  |  |
| SMLSIZE | small font |  |  |
| BOLD | bold font |  | Only color displays. This is a font size on its own - cannot be combined with other font size flags. |
| SHADOWED | shadow font |  | Only color displays |
| INVERS | inverted display |  |  |
| BLINK | blinking text |  |  |
| LEFT | left justify | 2.0.6 | Default for most functions not related to bitmaps |
| RIGHT | right justify |  |  |
| CENTER | center justify |  | Only color displays |
| VCENTER | center vertically | 2.5.0 | Only color displays |
| PREC1 | single decimal place |  |  |
| PREC2 | two decimal places |  |  |
| GREY\_DEFAULT | grey fill |  |  |
| TIMEHOUR | display hours |  | Only for drawTimer |

## Patterns

| Name | Description |
| :--- | :--- |
| FORCE | pixels will be black |
| ERASE | pixels will be white |
| DOTTED | lines will appear dotted |

