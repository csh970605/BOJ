# problem statement : https://www.acmicpc.net/problem/2583
import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x,y))
    extent = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n and graph[nx][ny] == 0:
                q.append((nx, ny))
                graph[nx][ny] = 1
                extent += 1
    return extent if extent>0 else 1


m, n, k = map(int, input().split())
graph = [[0]*n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[j][i] = 1
result = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            result.append(bfs(i, j))
print(len(result))
result.sort()
print(' '.join(map(str, result)))