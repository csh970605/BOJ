# problem statement : https://www.acmicpc.net/problem/7569
import sys
input = sys.stdin.readline
from collections import deque

def bfs(graph, m, n, h):
    q = deque()
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dh = [0, 0, 0, 0, 1, -1]
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 1:
                    q.append((i, j, k))
    while q:
        z, y, x = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dh[i]
            if 0<=nx<m and 0<=ny<n and 0<=nz<h and graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = graph[z][y][x] + 1
                q.append((nz, ny, nx))
    return graph

m, n, h = map(int, input().split())
graph = []
for _ in range(h):
    floor = []
    for _ in range(n):
        floor.append(list(map(int, input().split())))
    graph.append(floor)
graph = bfs(graph, m, n, h)

max_time = 0
for floor in graph:
    for row in floor:
        for value in row:
            if value == 0:
                print(-1)
                exit()
            max_time = max(max_time, value)
print(max_time-1)