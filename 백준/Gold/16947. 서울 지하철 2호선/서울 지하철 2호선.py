# problem statement : https://www.acmicpc.net/problem/16929
import sys
input = sys.stdin.readline
from collections import defaultdict, deque
sys.setrecursionlimit(1000000)

def dfs(node, parent_node):
    visited[node] = True
    for nn in graph[node]:
        if not visited[nn]:
            parent_nodes[nn] = node
            if dfs(nn, node):
                return True
        elif nn != parent_node and not cycle[nn]:
            cycle[node] = True
            temp_node = node
            while temp_node != nn:
                cycle[temp_node] = True
                temp_node = parent_nodes[temp_node]
            cycle[nn] = True
            return True
    return False
def bfs():
    q = deque()

    for i in range(1, n+1):
        if cycle[i]:
            distances[i] = 0
            q.append(i)
        
    while q:
        node = q.popleft()
        for nn in graph[node]:
            if distances[nn] == -1:
                distances[nn] = distances[node] + 1
                q.append(nn)

n = int(input())
graph = defaultdict(list)

for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0]*(n+1)
cycle = [0]*(n+1)
parent_nodes = [-1]*(n+1)
for i in range(n):
    if not visited[i]:
        if dfs(i, -1):
            break
distances = [-1]*(n+1)
bfs()
print(' '.join(map(str, distances[1:])))