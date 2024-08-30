# problem statement : https://www.acmicpc.net/problem/2468
import sys
input = sys.stdin.readline
from collections import deque
import copy

def bfs(x, y, safe, graph_cp):
    q = deque()
    q.append((x, y))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and graph_cp[nx][ny] > safe:
                q.append((nx, ny))
                graph_cp[nx][ny] = safe-1
    return 0
                

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
max_height = max(max(row) for row in graph)
max_value = 0
for m in range(max_height+1):
    sa = 0
    graph_cp = copy.deepcopy(graph)
    for i in range(n):
        for j in range(n):
            if graph_cp[i][j] > m:
                r = bfs(i, j, m, graph_cp)
                sa+=1
    max_value = max(max_value, sa)
print(max_value)