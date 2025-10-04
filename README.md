# FocusTrack (Study Timer App)

A simple study timer that helps students plan, track, and adjust study time by class.  
**Phase 1 goal:** a reliable countdown timer with basic session + break flow.

## Why
- I wanted a lightweight tool that:
  - Schedules study blocks by class
  - Tracks actual time vs. planned time
  - Rolls missed time forward to other days

## Roadmap (Phases)
- **Phase 1 – Core Timer (MVP)**
  - Start/Pause/Resume/Reset countdown
  - Session length input (e.g., 25m) + optional short break (5m)
  - Console or minimal UI output (time remaining, status)
- **Phase 2 – Sessions & Stats**
  - Log sessions to a simple file (CSV/JSON)
  - Show total minutes per class/day
- **Phase 3 – Planner**
  - Define classes + weekly plan
  - Auto-carry missed minutes to future days
- **Phase 4 – UI**
  - Basic desktop GUI (Tkinter) or web (Flask)
- **Phase 5 – Polishing**
  - Notifications, sounds, presets, export/share

## Tech (starting simple)
- Language: Python 3
- Phase 1: single-file script; no external deps

## Getting Started
1. `python3 --version` (ensure Python 3)
2. Run the MVP: `python focus_timer.py` (coming in Phase 1)
3. Hit Enter to start; `p` to pause/resume; `r` to reset (planned UX)

## Repo Structure (will grow)