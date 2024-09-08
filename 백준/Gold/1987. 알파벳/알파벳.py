# problem statement : https://www.acmicpc.net/problem/1987
import sys
input = sys.stdin.readline

def dfs(x, y, path_len, bitmask):
    global max_paths
    max_paths = max(max_paths, path_len)
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<r and 0<=ny<c and arr[nx][ny]:
            nc = ord(arr[nx][ny]) - ord('A')
            if not (bitmask & (1 << nc)):
                dfs(nx, ny, path_len+1, bitmask|(1<<nc))
r, c = map(int, input().split())
max_paths = 0
arr = []
for _ in range(r):
    arr.append(list(map(str, input().strip())))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

sc = (ord(arr[0][0])-ord('A'))
dfs(0, 0, 1, 1<<sc)
print(max_paths)