# problem statement : https://www.acmicpc.net/problem/14502
import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations
import copy


def bfs():
    q = deque()
    temp_arr = copy.deepcopy(arr)
    for i in range(n):
        for j in range(m):
            if temp_arr[i][j] == 2:
                q.append((i, j))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if temp_arr[nx][ny] == 0:
                    temp_arr[nx][ny] = 2
                    q.append((nx, ny))
    safe_area = 0
    for i in range(n):
        for j in range(m):
            if temp_arr[i][j] == 0:
                safe_area += 1
    
    return safe_area

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

empty_spaces = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            empty_spaces.append((i, j))

max_safe_area = 0
for walls in combinations(empty_spaces, 3):
    for x, y in walls:
        arr[x][y] = 1
    
    max_safe_area = max(max_safe_area, bfs())
    
    for x, y in walls:
        arr[x][y] = 0

print(max_safe_area)
