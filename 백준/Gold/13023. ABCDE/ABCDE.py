# problem statement : https://www.acmicpc.net/problem/13023
import sys
input = sys.stdin.readline
from collections import defaultdict
sys.setrecursionlimit(10000)

def dfs(x, depth):
    if depth == 4:
        print(1)
        exit()
    visited[x] = 1
    for neighbor in graph[x]:
        if not visited[neighbor]:
            dfs(neighbor, depth+1)
    visited[x] = False

n, m = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * n

for i in range(n):
    dfs(i, 0)

print(0)