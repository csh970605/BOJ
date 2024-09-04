# problem statement : https://www.acmicpc.net/problem/4963
import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<w and 0<=ny<h and not visited[ny][nx] and arr[ny][nx]:
                q.append((nx, ny))
                visited[ny][nx] = 1
while True:
    w, h = map(int, input().split())
    if (w, h) == (0, 0):
        break
    arr = []
    visited = [[0]*w for _ in range(h)]
    count = 0
    for _ in range(h):
        arr.append(list(map(int, input().split())))
    
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and not visited[i][j]:
                bfs(j, i)
                count+=1
    print(count)
                