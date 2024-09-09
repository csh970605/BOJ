# problem statement : https://www.acmicpc.net/problem/16948
import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y, count):
    q = deque()
    q.append((x, y, count))
    dx = [-2, -2, 0, 0, 2, 2]
    dy = [-1, 1, -2, 2, -1, 1]
    visited[x][y] = 1
    while q:
        x, y, count = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx, ny) == (x2, y2):
                return count + 1
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny, count+1))
    return -1
n = int(input())
chess_board = [[0]*n for _ in range(n)]
x1, y1, x2, y2 = map(int, input().split())
visited = [[0]*n for _ in range(n)]

print(bfs(x1, y1, 0))