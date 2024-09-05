# problem statement : https://www.acmicpc.net/problem/1967
import sys
input = sys.stdin.readline
from collections import defaultdict
sys.setrecursionlimit(1000000)

def dfs(node, weight):
    for nn, w in tree[node]:
        if not visited[nn]:
            result[nn] = weight + w
            visited[nn] = 1
            dfs(nn, result[nn])
n = int(input())
tree = defaultdict(list)
result = [0]*(n+1)
visited = [0]*(n+1)
visited[1] = 1
for i in range(n-1):
    a, b, c = map(int, input().split())
    tree[a].append([b, c])
    tree[b].append([a, c])
dfs(1, 0)
far_node = result.index(max(result))
result = [0]*(n+1)
visited = [0]*(n+1)
visited[far_node] = 1
dfs(far_node, 0)
print(max(result))