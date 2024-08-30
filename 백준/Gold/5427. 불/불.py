# problem statement : https://www.acmicpc.net/problem/5427
import sys
from collections import deque

input = sys.stdin.readline

def bfs(fire_queue, person_queue, graph, w, h):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = [[False] * w for _ in range(h)]

    while person_queue:
        for _ in range(len(fire_queue)):
            x, y = fire_queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == '.':
                    graph[nx][ny] = '*'
                    fire_queue.append((nx, ny))

        for _ in range(len(person_queue)):
            x, y, time = person_queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    return time + 1
                if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and graph[nx][ny] == '.':
                    visited[nx][ny] = True
                    person_queue.append((nx, ny, time + 1))

    return "IMPOSSIBLE"

t = int(input())
for _ in range(t):
    w, h = map(int, input().split())
    graph = [list(input().strip()) for _ in range(h)]
    
    fire_queue = deque()
    person_queue = deque()
    
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '*':
                fire_queue.append((i, j))
            elif graph[i][j] == '@':
                person_queue.append((i, j, 0))
                graph[i][j] = '.'
    
    result = bfs(fire_queue, person_queue, graph, w, h)
    print(result)
