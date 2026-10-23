from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import shutil
from typing import Iterable


ROOT = Path(__file__).resolve().parent.parent
DOCS_ROOT = ROOT / "website"
RADIOS_ROOT = DOCS_ROOT / "overview" / "radios"
RADIO_ASSETS_ROOT = DOCS_ROOT / "assets" / "radios"
WEBSIM_RADIOS_ROOT = ROOT.parent / "edgetx-websim" / "source-gfx" / "radios-white-bg-original"


@dataclass(frozen=True)
class RadioEntry:
    manufacturer: str
    manufacturer_slug: str
    model_label: str
    introduced: str
    lcd_type: str
    radio_id: str
    lcd_spec: str
    lua_radio_id: str | None = None

    @property
    def aliases(self) -> list[str]:
        return [part.strip() for part in self.model_label.split(" / ") if part.strip()]

    @property
    def primary_model(self) -> str:
        return self.aliases[0]

    @property
    def filename(self) -> str:
        if self.radio_id.startswith(f"{self.manufacturer_slug}-"):
            return f"{self.radio_id}.md"
        return f"{self.manufacturer_slug}-{self.radio_id}.md"

    @property
    def page_path(self) -> Path:
        return RADIOS_ROOT / self.manufacturer_slug / self.filename

    @property
    def route_path(self) -> str:
        return f"{self.filename.removesuffix('.md')}/"

    @property
    def image_name(self) -> str | None:
        return IMAGE_NAME_BY_ID.get(self.radio_id)

    @property
    def display_radio_id(self) -> str:
        return self.lua_radio_id or self.radio_id

    @property
    def display_radio_id_html(self) -> str:
        parts = [part.strip() for part in self.display_radio_id.split("/") if part.strip()]
        if len(parts) <= 1:
            return f"<code>{self.display_radio_id}</code>"
        return ", ".join(f"<code>{part}</code>" for part in parts)


RADIOS: tuple[RadioEntry, ...] = (
    RadioEntry("BetaFPV", "betafpv", "LiteRadio3 Pro", "-", "B&W LCD", "betafpv-literadio3-pro", "B&W LCD 128x64 1bit", "lr3pro"),
    RadioEntry("FatFish", "fatfish", "F16", "2.10", "Color LCD", "fatfish-f16", "Color LCD 480x272 RGB565", "f16"),
    RadioEntry("FlySky", "flysky", "EL18", "2.10", "Color LCD", "el18", "Color LCD 320x480 RGB565"),
    RadioEntry("FlySky", "flysky", "NB4+", "2.11", "Color LCD", "flysky-nb4-plus", "Color LCD 320x240 RGB565", "nb4p"),
    RadioEntry("FlySky", "flysky", "NV14", "2.10", "Color LCD", "flysky-nv14", "Color LCD 320x480 RGB565", "nv14"),
    RadioEntry("FlySky", "flysky", "PA01", "2.11", "Color LCD", "flysky-pa01", "Color LCD 320x240 RGB565", "pa01"),
    RadioEntry("FlySky", "flysky", "PL18 / PL18EV", "2.10", "Color LCD", "flysky-pl18-pl18ev", "Color LCD 480x320 RGB565", "pl18 / pl18ev"),
    RadioEntry("FlySky", "flysky", "PL18U", "2.11", "Color LCD", "flysky-pl18u", "Color LCD 480x320 RGB565"),
    RadioEntry("FlySky", "flysky", "ST16", "2.11", "Color LCD", "flysky-st16", "Color LCD 480x320 RGB565", "st16"),
    RadioEntry("FrSky", "frsky", "QX7 / QX7S / QX7 ACCESS / QX7S ACCESS", "2.10", "B&W LCD", "frsky-qx7-qx7s", "B&W LCD 128x64 1bit", "x7 / x7access"),
    RadioEntry("FrSky", "frsky", "X-Lite / X-Lite S / X-Lite Pro", "2.10", "B&W LCD", "frsky-x-lite-x-lite-s-x-lite-pro", "B&W LCD 128x64 1bit", "xlite / xlites"),
    RadioEntry("FrSky", "frsky", "X9 Lite / X9 Lite S", "2.10", "B&W LCD", "frsky-x9-lite-x9-lite-s", "B&W LCD 128x64 1bit", "x9lite / x9lites"),
    RadioEntry("FrSky", "frsky", "X9D / X9D+ / X9D SE", "2.10", "Grayscale LCD", "frsky-x9d-x9d-plus-x9d-plus-se", "Grayscale LCD 212x64 4bit", "x9d / x9d+"),
    RadioEntry("FrSky", "frsky", "X9D+ 2019 / X9D+ 2019 SE", "2.10", "Grayscale LCD", "x9dp2019", "Grayscale LCD 212x64 4bit"),
    RadioEntry("FrSky", "frsky", "X9E / X9E Hall", "2.10", "Grayscale LCD", "frsky-x9e-x9e-hall", "Grayscale LCD 212x64 4bit", "x9e"),
    RadioEntry("FrSky", "frsky", "X10 / X10S / X10 Express / X10S Express", "2.10", "Color LCD", "x10express", "Color LCD 480x272 RGB565", "x10 / x10express"),
    RadioEntry("FrSky", "frsky", "X12S / X12S IRSM", "2.10", "Color LCD", "frsky-x12s-x12s-irsm", "Color LCD 480x272 RGB565", "x12s"),
    RadioEntry("HelloRadioSky", "helloradiosky", "V12", "2.11", "Color LCD", "helloradiosky-v12", "Color LCD 480x272 RGB565", "v12"),
    RadioEntry("HelloRadioSky", "helloradiosky", "V14", "2.11", "B&W LCD", "helloradiosky-v14", "B&W LCD 128x64 1bit", "v14"),
    RadioEntry("HelloRadioSky", "helloradiosky", "V16", "2.11", "Color LCD", "helloradiosky-v16", "Color LCD 480x272 RGB565", "v16"),
    RadioEntry("iFlight", "iflight", "Commando8", "2.10", "B&W LCD", "iflight-commando8", "B&W LCD 480x272 1bit", "commando8"),
    RadioEntry("iFlight", "iflight", "Commando14", "-", "Color LCD", "iflight-commando14", "Color LCD 480x272 RGB565"),
    RadioEntry("Jumper", "jumper", "Bumblebee", "2.10", "B&W LCD", "jumper-bumblebee", "B&W LCD 128x64 1bit", "bumblebee"),
    RadioEntry("Jumper", "jumper", "T-Lite / T-Lite v2", "2.10", "B&W LCD", "jumper-t-lite-t-lite-v2", "B&W LCD 128x64 1bit", "tlite / tlitef4"),
    RadioEntry("Jumper", "jumper", "T-Pro", "2.10", "B&W LCD", "jumper-t-pro", "B&W LCD 128x64 1bit", "tpro / tprov2 / tpros"),
    RadioEntry("Jumper", "jumper", "T-12 / T12 Plus / T12 Pro Hall", "2.10", "B&W LCD", "jumper-t12-t12-plus-t12-pro-hall", "B&W LCD 128x64 1bit", "t12 / t12max"),
    RadioEntry("Jumper", "jumper", "T-14", "2.10", "B&W LCD", "jumper-t14", "B&W LCD 128x64 1bit", "t14"),
    RadioEntry("Jumper", "jumper", "T-20", "2.10", "B&W LCD", "jumper-t20", "B&W LCD 128x64 1bit", "t20"),
    RadioEntry("Jumper", "jumper", "T15", "2.10", "Color LCD", "t15", "Color LCD 480x320 RGB565"),
    RadioEntry("Jumper", "jumper", "T15 Pro", "2.12", "Color LCD", "jumper-t15-pro", "Color LCD 480x320 RGB565", "t15pro"),
    RadioEntry("Jumper", "jumper", "T16 / T16 Plus / T16 Pro Hall", "2.10", "Color LCD", "jumper-t16-t16-plus-t16-pro-hall", "Color LCD 480x272 RGB565", "t16"),
    RadioEntry("Jumper", "jumper", "T18 / T18 Lite / T18 Pro", "2.10", "Color LCD", "jumper-t18-t18-lite-t18-pro", "Color LCD 480x272 RGB565", "t18"),
    RadioEntry("Jumper", "jumper", "T20 V2", "2.10", "B&W LCD", "jumper-t20-v2", "B&W LCD 128x64 1bit", "t20v2"),
    RadioEntry("RadioMaster", "radiomaster", "Boxer", "2.10", "B&W LCD", "boxer", "B&W LCD 128x64 1bit"),
    RadioEntry("RadioMaster", "radiomaster", "GX12", "2.11", "B&W LCD", "radiomaster-gx12", "B&W LCD 128x64 1bit", "gx12"),
    RadioEntry("RadioMaster", "radiomaster", "MT12", "2.10", "B&W LCD", "radiomaster-mt12", "B&W LCD 128x64 1bit", "mt12"),
    RadioEntry("RadioMaster", "radiomaster", "Pocket", "2.10", "B&W LCD", "radiomaster-pocket", "B&W LCD 128x64 1bit"),
    RadioEntry("RadioMaster", "radiomaster", "T8 Pro", "-", "B&W LCD", "radiomaster-t8-pro", "B&W LCD 128x64 1bit", "t8"),
    RadioEntry("RadioMaster", "radiomaster", "TX12", "2.10", "B&W LCD", "radiomaster-tx12", "B&W LCD 128x64 1bit", "tx12"),
    RadioEntry("RadioMaster", "radiomaster", "TX12 Mark II", "2.10", "B&W LCD", "radiomaster-tx12-mark-ii", "B&W LCD 128x64 1bit", "tx12mk2"),
    RadioEntry("RadioMaster", "radiomaster", "Zorro", "2.10", "B&W LCD", "zorro", "B&W LCD 128x64 1bit"),
    RadioEntry("RadioMaster", "radiomaster", "TX15", "2.12", "Color LCD", "tx15", "Color LCD 480x320 RGB565"),
    RadioEntry("RadioMaster", "radiomaster", "TX16S / TX16S MAX / TX16S Mark II", "2.10", "Color LCD", "tx16s", "Color LCD 480x272 RGB565"),
    RadioEntry("RadioMaster", "radiomaster", "TX16S MK3 / TX16S MK3 MAX", "2.12", "Color LCD", "tx16smk3", "Color LCD 800x480 RGB565"),
)


IMAGE_NAME_BY_ID: dict[str, str] = {
    "betafpv-literadio3-pro": "betafpv-literadio-3-pro-500.png",
    "fatfish-f16": "fatfish-f16-500.png",
    "el18": "flysky-el18-500.png",
    "flysky-nb4-plus": "flysky-nb4-500.png",
    "flysky-nv14": "flysky-nv14-500.png",
    "flysky-pa01": "flysky-pa01-500.png",
    "flysky-pl18-pl18ev": "flysky-pl18-500.png",
    "flysky-pl18u": "flysky-pl18u-500.png",
    "flysky-st16": "flysky-st16-500.png",
    "frsky-qx7-qx7s": "frsky-qx7-500.png",
    "frsky-x-lite-x-lite-s-x-lite-pro": "frsky-xlite-pro-500.png",
    "frsky-x9-lite-x9-lite-s": "frsky-x9-lite-500.png",
    "frsky-x9d-x9d-plus-x9d-plus-se": "frsky-x9d-500.png",
    "x9dp2019": "frsky-x9d-2019-500.png",
    "frsky-x9e-x9e-hall": "frsky-x9e-500.png",
    "x10express": "frsky-x10-500.png",
    "frsky-x12s-x12s-irsm": "frsky-x12s-500.png",
    "helloradiosky-v12": "hrs-v12-500.png",
    "helloradiosky-v14": "hrs-v14-500.png",
    "helloradiosky-v16": "hrs-v16-500.png",
    "iflight-commando8": "iflight-commando-8-500.png",
    "iflight-commando14": "iflight-commando-14-500.png",
    "jumper-bumblebee": "jumper-bumblebee-500.png",
    "jumper-t-lite-t-lite-v2": "jumper-t-lite-500.png",
    "jumper-t-pro": "jumper-tpro-500.png",
    "jumper-t12-t12-plus-t12-pro-hall": "jumper-t12-500.png",
    "jumper-t14": "jumper-t14-500.png",
    "jumper-t20": "jumper-t20-500.png",
    "t15": "jumper-t15-500.png",
    "jumper-t15-pro": "jumper-t15-pro-500.png",
    "jumper-t16-t16-plus-t16-pro-hall": "jumper-t16-500.png",
    "jumper-t18-t18-lite-t18-pro": "jumper-t18-500.png",
    "jumper-t20-v2": "jumper-t20-500.png",
    "boxer": "radiomaster-boxer-500.png",
    "radiomaster-gx12": "radiomaster-gx12-500.png",
    "radiomaster-mt12": "radiomaster-mt12-500.png",
    "radiomaster-pocket": "radiomaster-pocket-500.png",
    "radiomaster-t8-pro": "radiomaster-t8pro-500.png",
    "radiomaster-tx12": "radiomaster-tx12-500.png",
    "radiomaster-tx12-mark-ii": "radiomaster-tx12-500.png",
    "zorro": "radiomaster-zorro-500.png",
    "tx15": "radiomaster-tx15-500.png",
    "tx16s": "radiomaster-tx16s-max-500.png",
    "tx16smk3": "radiomaster-tx16s-mk3-max-500.png",
}


def entries_for(manufacturer_slug: str) -> list[RadioEntry]:
    return [entry for entry in RADIOS if entry.manufacturer_slug == manufacturer_slug]


def link_label(entry: RadioEntry) -> str:
    return f"[{entry.model_label}]({entry.filename})"


def manufacturer_readme(manufacturer: str, manufacturer_slug: str, entries: Iterable[RadioEntry]) -> str:
    lines = [
        f"# {manufacturer}",
        "",
        '<table class="radio-list-table">',
            '<thead><tr><th>Model</th><th>from EdgeTX</th><th>LCD type</th></tr></thead>',
        '<tbody>',
    ]
    for entry in entries:
        if entry.image_name:
                model_cell = (
                    f'<div class="radio-list-model">'
                    f'<img src="../../../assets/radios/{entry.image_name}" alt="{entry.manufacturer} {entry.primary_model}">'
                    f'<a href="{entry.route_path}">{entry.model_label}</a>'
                    f'</div>'
                )
        else:
            model_cell = f'<a href="{entry.route_path}">{entry.model_label}</a>'
        lines.append(
            f"<tr><td>{model_cell}</td><td>{entry.introduced}</td><td>{entry.lcd_type}</td></tr>"
        )
    lines.extend(["</tbody>", "</table>", ""])
    return "\n".join(lines)


def radios_overview_readme(entries: Iterable[RadioEntry]) -> str:
    groups = (
        ("B&W LCD", "Radios with B&W LCD screen"),
        ("Grayscale LCD", "Radios with Grayscale LCD screen"),
        ("Color LCD", "Radios with COLOR LCD screen"),
    )

    lines = ["# Radios", ""]
    for lcd_type, heading in groups:
        lines.extend([f"## {heading}", ""])
        lines.extend(
            [
                '<table class="radio-list-table radio-overview-list-table">',
                '<thead><tr><th>Model</th><th>Manufacturer</th><th>from EdgeTX</th></tr></thead>',
                '<tbody>',
            ]
        )
        for entry in [item for item in entries if item.lcd_type == lcd_type]:
            if entry.image_name:
                model_cell = (
                    f'<div class="radio-list-model">'
                    f'<img src="../../assets/radios/{entry.image_name}" alt="{entry.manufacturer} {entry.primary_model}">'
                    f'<a href="{entry.manufacturer_slug}/{entry.route_path}">{entry.model_label}</a>'
                    f'</div>'
                )
            else:
                model_cell = f'<a href="{entry.manufacturer_slug}/{entry.route_path}">{entry.model_label}</a>'
            lines.append(
                f"<tr><td>{model_cell}</td><td>{entry.manufacturer}</td><td>{entry.introduced}</td></tr>"
            )
        lines.extend(["</tbody>", "</table>", ""])
    return "\n".join(lines)


def radio_page(entry: RadioEntry) -> str:
    rows = [
        ("Manufacturer", entry.manufacturer),
        ("Model", entry.primary_model),
    ]
    if len(entry.aliases) > 1:
        rows.append(("Versions", ", ".join(f"<code>{alias}</code>" for alias in entry.aliases[1:])))
    rows.extend([
        ("from EdgeTX", entry.introduced),
        ("LCD type", entry.lcd_spec),
        ("Radio ID", entry.display_radio_id_html),
    ])

    lines = [
        f"# {entry.manufacturer} {entry.primary_model}",
        "",
        f"[Back to {entry.manufacturer}](README.md) | [All radios](../README.md)",
        "",
        "## Overview",
        "",
        '<div class="radio-overview">',
        '<div class="radio-overview-image">',
    ]
    if entry.image_name:
        lines.extend(
            [
                f'<img src="../../../../assets/radios/{entry.image_name}" alt="{entry.manufacturer} {entry.primary_model}">',
                "</div>",
                '<div class="radio-overview-table">',
                "",
            ]
        )
    else:
        lines.extend(
            [
                "Picture not imported yet.",
                "</div>",
                '<div class="radio-overview-table">',
                "",
            ]
        )
    lines.extend(
        [
            '<table>',
            '<thead><tr><th>Property</th><th>Value</th></tr></thead>',
            '<tbody>',
        ]
    )
    for key, value in rows:
        lines.append(f"<tr><td>{key}</td><td>{value}</td></tr>")
    lines.extend(
        [
            "</tbody>",
            "</table>",
            "",
            "</div>",
            "</div>",
            "",
        ]
    )
    return "\n".join(lines)


def sync_images(entries: Iterable[RadioEntry]) -> None:
    RADIO_ASSETS_ROOT.mkdir(parents=True, exist_ok=True)
    for entry in entries:
        if not entry.image_name:
            continue
        source = WEBSIM_RADIOS_ROOT / entry.image_name
        target = RADIO_ASSETS_ROOT / entry.image_name
        if source.exists():
            shutil.copy2(source, target)


def main() -> None:
    RADIOS_ROOT.mkdir(parents=True, exist_ok=True)
    (RADIOS_ROOT / "README.md").write_text(
        radios_overview_readme(RADIOS),
        encoding="utf-8",
    )
    manufacturer_dirs = sorted({entry.manufacturer_slug for entry in RADIOS})
    for manufacturer_slug in manufacturer_dirs:
        entries = entries_for(manufacturer_slug)
        if not entries:
            continue
        manufacturer = entries[0].manufacturer
        target_dir = RADIOS_ROOT / manufacturer_slug
        target_dir.mkdir(parents=True, exist_ok=True)
        (target_dir / "README.md").write_text(
            manufacturer_readme(manufacturer, manufacturer_slug, entries),
            encoding="utf-8",
        )
        for entry in entries:
            entry.page_path.write_text(radio_page(entry), encoding="utf-8")
    sync_images(RADIOS)


if __name__ == "__main__":
    main()
