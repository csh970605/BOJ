# problem statement : https://www.acmicpc.net/problem/16940
import sys
input = sys.stdin.readline
from collections import defaultdict, deque
from itertools import combinations
def bfs(node):
    q = deque()
    q.append(node)
    visited[node] = True
    index = 1
    while q:
        node = q.popleft()
        neighbors = []
        for neighbor in graph[node]:
            if not visited[neighbor]:
                neighbors.append(neighbor)
                visited[neighbor] = True
        expected = bfs_order[index : index+len(neighbors)]
        if set(neighbors) != set(expected):
            return False
        neighbors_order = []
        for node in expected:
            q.append(node)
        index += len(neighbors)
    return True
n = int(input())
graph = defaultdict(list)
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
bfs_order = list(map(int, input().split()))
visited = [0]*(n+1)
if bfs_order[0] != 1:
    print(0)
else:
    if bfs(1):
        print(1)
    else:
        print(0)