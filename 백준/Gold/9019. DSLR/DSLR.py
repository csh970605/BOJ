# problem statement : https://www.acmicpc.net/problem/9019
import sys
input = sys.stdin.readline
from collections import deque

def bfs(x):
    q = deque()
    q.append((x, ''))
    visited[x] = 1
    dx = ['D', 'S', 'L', 'R']
    while q:
        x, command = q.popleft()
        for i in range(4):
            if i == 0:
                nx = (x*2)%10000
            elif i == 1:
                nx = (x-1)%10000
            elif i == 2:
                nx = (x%1000) * 10 + x // 1000
            elif i == 3:
                nx = (x // 10) + (x%10) * 1000
            if nx == target:
                return command+dx[i]
            if not visited[nx]:
                visited[nx] = 1
                q.append((nx, command+dx[i]))
    return -1
t = int(input())

for _ in range(t):
    start, target = map(int, input().split())
    visited = [0] * 10000
    print(bfs(start))