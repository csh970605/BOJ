# problem statement : https://www.acmicpc.net/problem/1463
import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, count):
    q = deque()
    q.append((x, count))
    visited[x] = 1
    while q:
        x, count = q.popleft()
        if x == 1:
            return count
        if x%3 == 0 and not visited[x//3]:
            q.append((x//3, count+1))
            visited[x//3] = 1
        if x%2 == 0 and not visited[x//2]:
            q.append((x//2, count+1))
            visited[x//2] = 1
        if x > 1 and not visited[x-1]:
            q.append((x-1, count+1))
            visited[x-1] = 1
n = int(input())
visited = [0] * (n+1)

print(bfs(n, 0))