# IAI_SLE2 — Profiling Report: BFS vs DFS

## 📌 Overview

This repository contains the code, profiling scripts, and results for **SLE-2 (Self Learning Evaluation 2)** of the course **02AML204 – Introduction to Artificial Intelligence** (SY B.Tech CSE AI & ML, Semester VI).

The goal of this SLE is to **empirically compare the performance of BFS and DFS** on the 8-Puzzle problem using Python's profiling tools.

---

## 🎯 Objective

- Measure real execution time of BFS and DFS
- Count nodes expanded, max frontier size, and path length
- Compare the two algorithms on the same problem
- Justify the results using data

---


---

## 🧩 Problem Used

**8-Puzzle problem** with:

| | |
|---|---|
| **Start State** | `(1, 2, 3, 4, 0, 6, 7, 5, 8)` |
| **Goal State** | `(1, 2, 3, 4, 5, 6, 7, 8, 0)` |

The same start and goal states were used for both algorithms to ensure a fair comparison.

---

## ⚙️ Profiling Method

| Parameter | Tool / Method |
|-----------|---------------|
| Execution Time | `time.perf_counter()` |
| Node Count | Manual counter inside search functions |
| Frontier Size | Queue/Stack length tracking |
| Runs | 3 per algorithm |
| Flame Graphs | `py-spy` |
| Python Version | 3.11 |

---

## 📊 Results

| Metric | BFS | DFS | Better? |
|--------|-----|-----|---------|
| **Avg. Time (ms)** | 0.0763 | 543.56 | ✅ BFS |
| **Nodes Expanded** | 9 | 135,586 | ✅ BFS |
| **Max Frontier** | 8 | 42,912 | ✅ BFS |
| **Path Length** | 3 | 49,285 | ✅ BFS |
| **Memory Usage** | Low | Very High | ✅ BFS |

> **Key Finding:** BFS was approximately **7,126× faster** than DFS on this problem.

---

## 🧠 Analysis

- **BFS** uses a queue (FIFO) and explores level-by-level — it guarantees the shortest path.
- **DFS** uses a stack (LIFO) and dives deep — it is memory-efficient but non-optimal.
- On the 8-Puzzle with a shallow solution (3 moves), BFS drastically outperformed DFS.
- For larger problems (e.g., 15-Puzzle), BFS memory grows exponentially, and DFS or A* becomes more practical.

---
