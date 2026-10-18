---
description: >-
  Many of the lcd functions accept parameters named flags and patterns. The
  names and their meanings are described below.
---

# Flags and Pattern Constants

## lcd.drawText Flags

| Name | Description | EdgeTX ver | Notes |
| :--- | :--- | :--- | :--- |
| `0` | normal font, default precision for numeric | 2.3 |  |
| `XXLSIZE` | jumbo font | 2.3 |  |
| `DBLSIZE` | double size font | 2.3 |  |
| `MIDSIZE` | mid sized font | 2.3 |  |
| `SMLSIZE` | small font | 2.3 |  |
| `BOLD` | bold font | 2.3 | Only color displays. This is a font size on its own - cannot be combined with other font size flags. |
| `SHADOWED` | shadow font | 2.3 | Only color displays |
| `INVERS` | inverted display | 2.3 |  |
| `BLINK` | blinking text | 2.3 |  |
| `LEFT` | left justify | 2.3 | Default for most functions not related to bitmaps |
| `RIGHT` | right justify | 2.3 |  |
| `CENTER` | center justify | 2.3 | Only color displays |
| `VCENTER` | center vertically | 2.5.0 | Only color displays |
| `PREC1` | single decimal place | 2.3 | display with one decimal place (number 386 is displayed as 38.6) |
| `PREC2` | two decimal places | 2.3 | display with one decimal place (number 386 is displayed as 3.86) |
| `GREY_DEFAULT` | grey fill | 2.3 |  |
| `TIMEHOUR` | display hours | 2.3 | Only for lcd/drawTimer |

## lcd drawing functions flags on B&W LCD radios

| Name | Description | EdgeTX ver | Notes |
| :--- | :--- | :--- | :--- |
| `FORCE` | pixels will be black | 2.3 |  |
| `ERASE` | pixels will be white | 2.3 |  |

## lcd.drawLine function patterns

| Name | Description | EdgeTX ver | Notes |
| :--- | :--- | :--- | :--- |
| `SOLID` | lines will appear soild | 2.3 |  |
| `DOTTED` | lines will appear dotted | 2.3 |  |
