# Mewgenics Breeding Manager

An external breeding and roster manager for [Mewgenics](https://store.steampowered.com/app/686060/Mewgenics/) — similar to Dwarf Therapist for Dwarf Fortress.

Reads your save file live and gives you a clear view of every cat's stats, room, abilities, mutations, and lineage so you can make smarter breeding decisions without alt-tabbing.

> **Note:** This tool was vibecoded. The family tree and inbreeding analysis features are not guaranteed to be accurate. They can be enabled via **Settings → Show Family Tree & Inbreeding** (off by default).

![screenshot](screenshot.png)

## Features

- **Live save reading** — watches the save file and reloads automatically when the game writes
- **Full cat roster** — all cats in one sortable table; filter by room, adventure, or gone (with counts)
- **Color-coded base stats** — red (1) → grey (4) → green (7) at a glance
- **Detail panel** — click any cat to see abilities, mutations, and lineage; hover chips for descriptions
- **Breeding comparison** — Ctrl+click two cats to see offspring stat ranges and combined mutations
- **Search bar** — filter cats by name in real time
- **Family tree & inbreeding** (optional) — toggle in Settings; shows Gen depth, Source column, inbreeding score, shared-ancestor warnings, and risky-pair lowlighting

## Requirements

- Python 3.11+
- [PySide6](https://pypi.org/project/PySide6/)
- [lz4](https://pypi.org/project/lz4/)

## Installation

```bash
git clone https://github.com/frankieg33/MewgenicsBreedingManager
cd MewgenicsBreedingManager
pip install -r requirements.txt
python mewgenics_manager.py
```

Or on Windows, double-click **build.bat** to build a standalone `.exe` via PyInstaller.

## Usage

The app auto-detects your save file from:
```
%APPDATA%\Glaiel Games\Mewgenics\<SteamID>\saves\
```

Use **File → Open Save File** to load a different save, or **File → Reload** (F5) to force a refresh.

### Roster table
| Column | Description |
|--------|-------------|
| Name | Cat's name |
| ♀/♂ | Gender |
| Room | Current room in the house |
| Status | `House` / `Away` (adventure) / `Gone` |
| STR–LCK | Base (heritable) stats, color coded |
| Sum | Sum of all base stats |
| Abilities | Active abilities |
| Mutations | Passive mutation traits |
| Gen / Source / Inbr | Lineage columns (visible when toggled on) |

Hover a stat cell to see base vs. total (including equipment bonuses).
Hover an ability or mutation chip to see what it does.

### Detail panel
- **1 cat selected** — shows abilities, mutations, equipment, and known lineage
- **2 cats selected (Ctrl+click)** — shows a breeding comparison with per-stat offspring ranges and combined mutations

### Sidebar filters
- **All Cats** — every cat including gone
- **Alive** — in house + adventure cats
- **Room buttons** — dynamically generated for each occupied room (with cat counts)
- **On Adventure** — cats currently in a run
- **Gone** — dead/sold cats

## Notes

Parent links are resolved from the pedigree stored in the save file. The family tree and inbreeding features are experimental — they can be wrong, especially for cats with complex lineage or saves that have been running for a long time. Enable them via **Settings → Show Family Tree & Inbreeding**.

## Credits

Save file parsing based on [pzx521521/mewgenics-save-editor](https://github.com/pzx521521/mewgenics-save-editor) and community research on the Mewgenics save format.
