# problem statement : https://www.acmicpc.net/problem/2146
import sys
input = sys.stdin.readline
from collections import deque
def bfs(x, y, id):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    group[x][y] = id
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    group[nx][ny] = id

def bridge(group_id):
    queue = deque()
    dist = [[-1]*n for _ in range(n)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(n):
        for j in range(n):
            if group[i][j] == group_id:
                queue.append((i, j))
                dist[i][j] = 0
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if group[nx][ny] > 0 and group[nx][ny] != group_id:
                    return dist[x][y]
                if graph[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
    return float('inf')

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
visited = [[0]*n for _ in range(n)]
count = 1
group = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1:
            bfs(i, j, count)
            count += 1

min_distance = float('inf')
for i in range(1, count):
    min_distance = min(min_distance, bridge(i))

print(min_distance)