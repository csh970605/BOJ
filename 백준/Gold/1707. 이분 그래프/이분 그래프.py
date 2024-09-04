# problem statement : https://www.acmicpc.net/problem/1707
import sys
input = sys.stdin.readline
from collections import defaultdict
sys.setrecursionlimit(1000000)

def dfs(x, color):
    visited[x] = color
    for neighbor in graph[x]:
        if visited[neighbor] == 0:
            if not dfs(neighbor, -color):
                return False
        elif visited[neighbor] == visited[x]:
                return False
    return True

n = int(input())

for _ in range(n):
    v, e = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [0]*(v+1)
    check = True
    for i in range(1, v+1):
        if visited[i] == 0:
            if not dfs(i, 1):
                check = False
                break
    if check:
        print('YES')
    else:
        print('NO')