# problem statement : https://www.acmicpc.net/problem/10026
import sys
input = sys.stdin.readline
from collections import deque

def bfs(z, y, x):
    q = deque()
    q.append((x, y, z))
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0<=nx<c and 0<=ny<r and 0<=nz<l:
                if graph[nz][ny][nx] == 'E':
                    return graph[z][y][x]+1
                elif graph[nz][ny][nx] == 0:
                    q.append((nx, ny, nz))
                    graph[nz][ny][nx] = graph[z][y][x]+1
    return '-1'

while True:
    l, r, c = map(int, input().split())
    if (l, r, c) == (0, 0, 0):
        break
    graph = []
    for i in range(l):
        floor = []
        for j in range(r):
            temp = list(map(str, input().strip()))
            for k in range(c):
                if temp[k] == 'S':
                    start_point = (i, j, k)
                    temp[k] = 0
                elif temp[k] == '.':
                    temp[k] = 0
                elif temp[k] == '#':
                    temp[k] = 1
            floor.append(temp)
        graph.append(floor)
        trash = input()
    result = bfs(start_point[0], start_point[1], start_point[2])
    if result == '-1':
        print('Trapped!')
    else:
        print(f'Escaped in {result} minute(s).')

