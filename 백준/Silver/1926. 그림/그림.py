# problem statement : https://www.acmicpc.net/problem/1926
import sys
input = sys.stdin.readline
from collections import deque
def bfs(arr, a, b):
    q = deque()
    q.append((a, b))
    arr[a][b] = 0
    count = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if arr[nx][ny] == 1:
                arr[nx][ny] = 0
                q.append((nx, ny))
                count += 1
    return count

n, m = list(map(int, input().split()))
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

count = 0
max_value = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            count += 1
            max_value = max(bfs(arr, i, j), max_value)

print(count)
print(max_value)