# problem statement : https://www.acmicpc.net/problem/1939
import sys
input = sys.stdin.readline
from collections import defaultdict, deque

def bfs(graph, start, end, mid_weight):
    q = deque()
    q.append(start)
    visited = set()
    visited.add(start)
    while q:
        node = q.popleft()
        if node == end:
            return True
        for neighbor, weight in graph[node]:
            if neighbor not in visited and weight>=mid_weight:
                visited.add(neighbor)
                q.append(neighbor)
    
    return False

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

start, end = map(int, input().split())
low = 1
high = 1000000000
result = low

while low <= high:
    mid = (low+high) // 2
    if bfs(graph, start, end, mid):
        result = mid
        low = mid + 1
    else:
        high = mid - 1
print(result)