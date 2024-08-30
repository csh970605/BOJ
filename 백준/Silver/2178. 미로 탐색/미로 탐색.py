# problem statement : https://www.acmicpc.net/problem/2178
import sys
input = sys.stdin.readline
from collections import deque

def dfs(graph, x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
    return graph

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().strip())))
graph = dfs(graph, 0, 0)
print(graph[n-1][m-1])