# problem statement : https://www.acmicpc.net/problem/7576
import sys
input = sys.stdin.readline
from collections import deque

def bfs(graph):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                q.append((j, i))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                q.append((nx, ny))
    return graph

m, n = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

graph = bfs(graph)
max_time = 0

for row in graph:
    for value in row:
        if value == 0:
            print(-1)
            exit()
        max_time = max(max_time, value)
print(max_time-1)