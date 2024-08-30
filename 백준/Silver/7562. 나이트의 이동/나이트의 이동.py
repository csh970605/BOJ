# problem statement : https://www.acmicpc.net/problem/7562
import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    graph = [[0]*length for _ in range(length)]
    graph[x][y] = 1
    dx = [2, 2, 1, 1, -1, -1, -2, -2]
    dy = [1, -1, 2, -2, 2, -2, 1, -1]
    count = 0
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<length and 0<=ny<length:
                if (nx, ny) == (target_x, target_y):
                    return graph
                elif graph[nx][ny] == 0:
                    count+=1
                    q.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1
    return count
t = int(input())
for _ in range(t):
    length = int(input())
    orin_x, orin_y = map(int, input().split())
    target_x, target_y = map(int, input().split())
    if (orin_x, orin_y) == (target_x, target_y):
        print(0)
    else:
        max_value = 0
        graph = bfs(orin_x, orin_y)
        for row in graph:
            for value in row:
                max_value = max(max_value, value)
        print(max_value-1)
