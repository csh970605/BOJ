# problem statement : https://www.acmicpc.net/problem/1260
import sys
input = sys.stdin.readline
from collections import defaultdict, deque

def dfs(x):
    print(x, end=' ')
    visited[x] = 1
    for neighbor in graph[x]:
        if not visited[neighbor]:
            dfs(neighbor)
def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1
    while q:
        nn = q.popleft()
        print(nn, end=' ')
        for neighbor in graph[nn]:
            if not visited[neighbor]:
                q.append(neighbor)
                visited[neighbor] = 1
n, m, v = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for key in graph:
    graph[key].sort()

visited = [0]*(n+1)
dfs(v)
print()
visited = [0]*(n+1)
bfs(v)