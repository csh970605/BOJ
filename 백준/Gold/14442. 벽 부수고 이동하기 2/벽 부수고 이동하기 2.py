# problem statement : https://www.acmicpc.net/problem/14442
import sys
input = sys.stdin.readline
from collections import deque

def bfs(goal_x, goal_y):
    q = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = [[[0]*(k+1) for _ in range(goal_y)] for _ in range(goal_x)]
    q.append((0, 0, 0))
    visited[0][0][0] = 1

    while q:
        x, y, crash = q.popleft()

        if x==goal_x-1 and y==goal_y-1:
            return visited[x][y][crash]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<goal_x and 0<=ny<goal_y:
                if graph[nx][ny]==0 and visited[nx][ny][crash]==0:
                    visited[nx][ny][crash] = visited[x][y][crash] + 1
                    q.append((nx, ny, crash))
                
                if graph[nx][ny]==1 and crash<k and visited[nx][ny][crash+1]==0:
                    visited[nx][ny][crash+1] = visited[x][y][crash] + 1
                    q.append((nx, ny, crash+1))
    return -1

w, h, k = map(int, input().split())
graph = []
for _ in range(w):
    graph.append(list(map(int, input().strip())))

result = bfs(w, h)
print(result)
