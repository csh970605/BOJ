# problem statement : https://www.acmicpc.net/problem/1261
import sys
input = sys.stdin.readline
from collections import defaultdict, deque

def bfs():
    q = deque()
    q.append(1)
    visited[1] = True
    while q :
        node = q.popleft()
        for neighbor in tree[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                result[neighbor] = node
                q.append(neighbor)

n = int(input())
tree = defaultdict(list)
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
result = [0]*(n+1)

visited = [0]*(n+1)
bfs()
for i in range(2, n+1):
    print(result[i])