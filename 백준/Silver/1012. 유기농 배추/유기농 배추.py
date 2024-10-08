# problem statement : https://www.acmicpc.net/problem/1012
import sys
input = sys.stdin.readline
from collections import deque

def dfs(x, y):
    q = deque()
    q.append((x, y))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))

graph = []
t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        a, b = map(int ,input().split())
        graph[b][a] = 1
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                count+=1
                dfs(i, j)
    print(count)