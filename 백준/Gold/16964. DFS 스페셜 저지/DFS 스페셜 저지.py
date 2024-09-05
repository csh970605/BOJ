# problem statement : https://www.acmicpc.net/problem/16964
import sys
input = sys.stdin.readline
from collections import defaultdict
sys.setrecursionlimit(1000000)

def dfs(node):
    visited[node] = True
    result.append(node)
    for nn in graph[node]:
        if not visited[nn]:
            dfs(nn)



n = int(input())
graph = defaultdict(list)
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
dfs_order = list(map(int, input().split()))
if dfs_order[0] != 1:
    print(0)
    exit()
order = [0]*(n+1)
for i in range(n):
    order[dfs_order[i]] = i
for i in range(1, n + 1):
    graph[i].sort(key=lambda x: order[x])
result = []
visited = [0]*(n+1)
dfs(1)
if result == dfs_order:
    print(1)
else:
    print(0)