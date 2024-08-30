# problem statement : https://www.acmicpc.net/problem/2667
import sys
input = sys.stdin.readline
from collections import deque
def bfs(x, y):
    q = deque()
    q.append((x, y))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    dong = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = 0
                dong += 1
    if dong == 0:
        dong = 1
    return dong


n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().strip())))
result = []
for i in range(n):
    for j in range(n):
        if graph[i][j]:
           result.append(bfs(i, j)) 
result.sort()
print(len(result))
print('\n'.join(map(str,result)))