# problem statement : https://www.acmicpc.net/problem/10026
import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y, target, graph):
    q = deque()
    q.append((x, y, target))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        x, y, target = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] == target:
                graph[nx][ny] = 0
                q.append((nx, ny, target))

n = int(input())
orin_graph = []
eye_graph = []
for _ in range(n):
    string = input().strip()
    orin_list = []
    eye_list = []
    for s in string:
        if s == 'B':
            orin_list.append(s)
            eye_list.append(s)
        else:
            orin_list.append(s)
            eye_list.append('R')
    orin_graph.append(orin_list)
    eye_graph.append(eye_list)

orin_result = 0
eye_result = 0
for i in range(n):
    for j in range(n):
        if orin_graph[i][j] == 'R':
            bfs(i, j, 'R', orin_graph)
            orin_result+=1
        elif orin_graph[i][j] == 'G':
            bfs(i, j, 'G', orin_graph)
            orin_result+=1
        elif orin_graph[i][j] == 'B':
            bfs(i, j, 'B', orin_graph)
            orin_result+=1
        if eye_graph[i][j] == 'R':
            bfs(i, j, 'R', eye_graph)
            eye_result+=1
        elif eye_graph[i][j] == 'B':
            bfs(i, j, 'B', eye_graph)
            eye_result+=1
print(orin_result, eye_result)