"""
SLE-2: BFS (Breadth-First Search) on the 8-Puzzle Problem
Course: 02AML204 - Introduction to Artificial Intelligence

TIME COMPLEXITY:
    Best case    : O(b^d)  -> goal found at shallow depth
    Average case : O(b^d)  -> explores level by level
    Worst case   : O(b^d)  -> explores entire space
    Space        : O(b^d)  -> ALL frontier nodes stored
    where b = branching factor, d = depth of shallowest goal
"""

import time
from collections import deque

nodes_expanded = 0
max_frontier = 0


def get_neighbors(state):
    state = list(state)
    idx = state.index(0)
    row, col = divmod(idx, 3)
    moves = []
    if row > 0:
        s = state.copy()
        s[idx], s[idx - 3] = s[idx - 3], s[idx]
        moves.append((tuple(s), "UP"))
    if row < 2:
        s = state.copy()
        s[idx], s[idx + 3] = s[idx + 3], s[idx]
        moves.append((tuple(s), "DOWN"))
    if col > 0:
        s = state.copy()
        s[idx], s[idx - 1] = s[idx - 1], s[idx]
        moves.append((tuple(s), "LEFT"))
    if col < 2:
        s = state.copy()
        s[idx], s[idx + 1] = s[idx + 1], s[idx]
        moves.append((tuple(s), "RIGHT"))
    return moves


def bfs(start, goal):
    global nodes_expanded, max_frontier
    nodes_expanded = 0
    max_frontier = 0

    frontier = deque([start])
    visited = {start}
    parent = {start: None}

    while frontier:
        max_frontier = max(max_frontier, len(frontier))
        current = frontier.popleft()
        nodes_expanded += 1

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]

        for nxt, _ in get_neighbors(current):
            if nxt not in visited:
                visited.add(nxt)
                parent[nxt] = current
                frontier.append(nxt)
    return None


if __name__ == "__main__":
    start = (1, 2, 3,
             4, 0, 6,
             7, 5, 8)
    goal  = (1, 2, 3,
             4, 5, 6,
             7, 8, 0)

    t0 = time.perf_counter()
    path = bfs(start, goal)
    t1 = time.perf_counter()

    print("=" * 55)
    print("BFS on 8-Puzzle")
    print("=" * 55)
    print(f"Time taken      : {(t1 - t0) * 1000:.3f} ms")
    print(f"Nodes expanded  : {nodes_expanded}")
    print(f"Max frontier    : {max_frontier}")
    print(f"Path length     : {len(path) if path else 'Not found'}")