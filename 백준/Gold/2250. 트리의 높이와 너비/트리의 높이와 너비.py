# problem statement : https://www.acmicpc.net/problem/2250
import sys
input = sys.stdin.readline

def dfs(node, depth):
    global current_width
    if node == -1:
        return
    
    if left[node] != -1:
        dfs(left[node], depth+1)
    
    depth_list[node] = depth
    current_width += 1
    width[node] = current_width
    level_min[depth] = min(level_min[depth], current_width)
    level_max[depth] = max(level_max[depth], current_width)
    if right[node] != -1:
        dfs(right[node], depth+1)
n = int(input())
left = {}
right = {}
parent = [0] * (n + 1)
for _ in range(n):
    a, b, c = map(int, input().split())
    left[a] = b
    right[a] = c
    if b != -1:
        parent[b] = a
    if c != -1:
        parent[c] = a

root = 1
level_min = [float('inf')]*(n+1)
level_max = [0]*(n+1)
for i in range(1, n + 1):
    if parent[i] == 0:
        root = i
        break

depth_list = [0]*(n+1)
width = [0]*(n+1)
current_width = 0
dfs(root, 1)
max_width = 0
best_level = 0
for i in range(1, n + 1):
    if level_max[i] != 0:
        width_of_level = level_max[i] - level_min[i] + 1
        if width_of_level > max_width:
            max_width = width_of_level
            best_level = i
print(best_level, max_width)