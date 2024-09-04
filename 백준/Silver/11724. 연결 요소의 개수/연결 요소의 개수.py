# problem statement : https://www.acmicpc.net/problem/11724
import sys
input = sys.stdin.readline
from collections import defaultdict, deque

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1
    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = 1
                q.append(neighbor)

n, m = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for key in graph:
    graph[key].sort()
visited = [0] * (n+1)

count = 0
for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        count += 1
print(count)