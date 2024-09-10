# problem statement : https://www.acmicpc.net/problem/3055
import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y, count):
    q = deque()
    q.append((x, y, count))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        new_water = []
        for wx, wy in water:
            for i in range(4):
                nwx = wx + dx[i]
                nwy = wy + dy[i]
                if 0 <= nwx < R and 0 <= nwy < C and arr[nwx][nwy] == '.':
                    arr[nwx][nwy] = '*'
                    new_water.append((nwx, nwy))
        water[:] = new_water

        for _ in range(len(q)):
            x, y, count = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < R and 0 <= ny < C:
                    if arr[nx][ny] == 'D':
                        return count + 1
                    if arr[nx][ny] == '.':
                        arr[nx][ny] = 'S'
                        q.append((nx, ny, count + 1))
    return "KAKTUS"
R, C = map(int, input().split())
arr = []
water = []
for i in range(R):
    inputs = list(map(str, input().strip()))
    arr.append(inputs)
    for j in range(C):
        if arr[i][j] == 'S':
            start = (i, j)
        elif arr[i][j] == '*':
            water.append([i, j])
print(bfs(start[0], start[1], 0))