"""Runs BFS many times so py-spy has time to sample."""
from bfs import bfs

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)
goal  = (1, 2, 3,
         4, 5, 6,
         7, 8, 0)

for _ in range(20000):
    bfs(start, goal)