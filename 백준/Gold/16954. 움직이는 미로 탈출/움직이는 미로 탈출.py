# problem statement : https://www.acmicpc.net/problem/16954
import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    q = deque()
    q.append((7, 0, 0))
    dx = [0, 1, 1, 0, -1, -1, -1, 0, 1]
    dy = [0, 0, 1, 1, 1, 0, -1, -1, -1]
    while q:
        x, y, time = q.popleft()

        if (x, y) == (0, 7):
            return 1

        for i in range(9):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 8 and 0 <= ny < 8:
                if nx-time >= 0 and arr[nx-time][ny] == '#':
                    continue

                if nx-time-1 >= 0 and arr[nx-time-1][ny] == '#':
                    continue
                
                q.append((nx, ny, time+1))

        if time >= 8:
            return 1

    return 0


arr = []
visited = [[0] * 8 for _ in range(8)]
visited[7][0] = 1

for i in range(8):
    arr.append(list(input().strip()))

print(bfs())