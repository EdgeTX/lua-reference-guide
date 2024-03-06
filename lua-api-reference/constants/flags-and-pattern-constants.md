---
description: >-
  Many of the lcd functions accept parameters named flags and patterns. The
  names and their meanings are described below.
---

# Flags and Pattern Constants

## lcd.drawText Flags

<table><thead><tr><th width="177">Name</th><th width="191">Description</th><th width="119">EdgeTX ver</th><th>Notes</th></tr></thead><tbody><tr><td>0</td><td>normal font, default precision for numeric</td><td>2.3</td><td></td></tr><tr><td>XXLSIZE</td><td>jumbo font</td><td>2.3</td><td></td></tr><tr><td>DBLSIZE</td><td>double size font</td><td>2.3</td><td></td></tr><tr><td>MIDSIZE</td><td>mid sized font</td><td>2.3</td><td></td></tr><tr><td>SMLSIZE</td><td>small font</td><td>2.3</td><td></td></tr><tr><td>BOLD</td><td>bold font</td><td>2.3</td><td>Only color displays. This is a font size on its own - cannot be combined with other font size flags.</td></tr><tr><td>SHADOWED</td><td>shadow font</td><td>2.3</td><td>Only color displays</td></tr><tr><td>INVERS</td><td>inverted display</td><td>2.3</td><td></td></tr><tr><td>BLINK</td><td>blinking text</td><td>2.3</td><td></td></tr><tr><td>LEFT</td><td>left justify</td><td>2.3</td><td>Default for most functions not related to bitmaps</td></tr><tr><td>RIGHT</td><td>right justify</td><td>2.3</td><td></td></tr><tr><td>CENTER</td><td>center justify</td><td>2.3</td><td>Only color displays</td></tr><tr><td>VCENTER</td><td>center vertically</td><td>2.5.0</td><td>Only color displays</td></tr><tr><td>PREC1</td><td>single decimal place</td><td>2.3</td><td>display with one decimal place (number 386 is displayed as 38.6)</td></tr><tr><td>PREC2</td><td>two decimal places</td><td>2.3</td><td>display with one decimal place (number 386 is displayed as 3.86)</td></tr><tr><td>GREY_DEFAULT</td><td>grey fill</td><td>2.3</td><td></td></tr><tr><td>TIMEHOUR</td><td>display hours</td><td>2.3</td><td>Only for lcd/drawTimer</td></tr></tbody></table>

## lcd drawing functions flags on B\&W LCD radios

<table><thead><tr><th width="173">Name</th><th width="196">Description</th><th width="125">EdgeTX ver</th><th>Notes</th></tr></thead><tbody><tr><td>FORCE</td><td>pixels will be black</td><td>2.3</td><td></td></tr><tr><td>ERASE</td><td>pixels will be white</td><td>2.3</td><td></td></tr></tbody></table>

## lcd.drawLine function patterns

<table><thead><tr><th width="173">Name</th><th width="205">Description</th><th width="122">EdgeTX ver</th><th>Notes</th></tr></thead><tbody><tr><td>SOLID</td><td>lines will appear soild</td><td>2.3</td><td></td></tr><tr><td>DOTTED</td><td>lines will appear dotted</td><td>2.3</td><td></td></tr></tbody></table>
