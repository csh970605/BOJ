# problem statement : https://www.acmicpc.net/problem/2573
import sys
input = sys.stdin.readline
from collections import deque
def bfs(x, y, visited):
    q = deque()
    q.append((x, y))
    temp = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    graph[x][y] -= 1
                    if graph[x][y] == 0:
                        graph[x][y] = -1
                        temp.append([x, y])
                elif graph[nx][ny] > 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                
    for x, y in temp:
        graph[x][y] = 0
    return visited



n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

result = 0
while True:
    visited = [[0]*m for _ in range(n)]
    count = 0
    check = True
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0 and not visited[i][j]:
                if count == 1:
                    check = False
                    break
                bfs(i, j, visited)
                count += 1
    if check and count == 0:
        print(0)
        break
    elif not check:
        print(result)
        break
    result += 1