# problem statement : https://www.acmicpc.net/problem/1261
import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<m and 0<=ny<n:
                if graph[nx][ny] == 0 and visited[nx][ny] > visited[x][y]:
                    visited[nx][ny] = visited[x][y]
                    q.appendleft((nx, ny))
                elif graph[nx][ny] == 1 and visited[nx][ny] > visited[x][y]+1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

n, m = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(list(map(int, input().strip())))
visited = [[float('inf')]*n for _ in range(m)]
bfs()
print(visited[m-1][n-1])