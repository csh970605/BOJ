# problem statement : https://www.acmicpc.net/problem/16236
import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y, shark_size):
    q = deque()
    q.append((x, y, 0))
    visited = [[0]*n for _ in range(n)]
    visited[x][y] = 1
    possibles = []
    min_distance = float('inf')
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y, distance = q.popleft()

        if distance > min_distance:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if arr[nx][ny] <= shark_size:
                    visited[nx][ny] = 1
                    q.append((nx, ny, distance+1))
                    if 0 < arr[nx][ny] < shark_size:
                        possibles.append([distance+1, nx, ny])
                        min_distance = distance + 1
    possibles.sort()
    if possibles:
        return possibles[0]
    else:
        return None


n = int(input())
arr = []
for i in range(n):
    inputs = list(map(int, input().split()))
    arr.append(inputs)
    for j in range(n):
        if arr[i][j] == 9:
            start = (i, j)
            arr[i][j] = 0
shark_size = 2
eaten_fish = 0
count = 0

while True:
    result = bfs(start[0], start[1], shark_size)

    if not result:
        print(count)
        break

    distance, fish_x, fish_y = result
    start = (fish_x, fish_y)
    count += distance
    arr[fish_x][fish_y] = 0
    eaten_fish += 1

    if eaten_fish == shark_size:
        shark_size += 1
        eaten_fish = 0
