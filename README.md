# 🔬 Systems Architecture & Engineering Lab

This repository serves as a dedicated engineering sandbox for deep-diving into modern language paradigms, advanced algorithmic efficiency, and operating system scheduling mechanics.

## 🎯 Objectives
1. **Algorithmic Profiling (Python):** Benchmarking execution runtime, analyzing memory footprints (`line_profiler`), and optimizing time/space complexity ($O(N)$ vs $O(1)$ mechanics).
2. **Concurrent Systems Prototyping (Go):** Exploring compiled language performance, explicit memory/pointer management, and multi-threaded CSP concurrency models (Goroutines/Channels).
3. **OS Kernel Research (Linux):** Deconstructing low-level operating system architectures, resource allocation, and advanced task scheduling frameworks (EEVDF/CFS internals).

---

## 📂 Repository Structure

```
python-systems-foundation/
├── .github/
│   └── workflows/
│       └── run_tests.yml          # Automates code health checks
├── datacamp_tracks/               # Tracks your structured DataCamp courses
│   ├── 01_python_developer/
│   │   ├── ch01_efficiencies/
│   │   ├── ch02_timing_profiling/
│   │   └── ch10_dsa/
│   └── README.md                  # Quick notes on course completion dates
├── basic_concepts/                # Your independent practice ground
│   ├── 01_control_flow/
│   ├── 02_collections/            # (Lists, Dicts, Sets)
│   ├── 03_functions/
│   └── scratchpad.py              # Quick throwaway code tests
├── .gitignore                      # Prevents junk files from being tracked
├── progress_log.md                # Your master context switcher (Crucial!)
└── README.md                       # The main dashboard of your repo
```

---

## 💡 How to Maintain Momentum using this Repo

* **The 1-Line Commit Habit:** When you finish a single DataCamp exercise or write a basic practice script, commit it immediately. Use small, micro-commits:
```bash
git commit -m "feat: complete dictionary frequency counter exercise"
```

* **The "Drop-Everything" Routine:** If a cluster alert fires or your manager reaches out with an urgent operational issue, open `progress_log.md`, type out your exact line number and current thought in the Active Brain Dump, run `git commit -am "checkpoint: saving context before operational shift"`, and close your laptop.
When you return hours or days later, a single glance at your GitHub dashboard tells you precisely what your next keystroke needs to be.
