# problem statement : https://www.acmicpc.net/problem/16929
import sys
input = sys.stdin.readline

def dfs(x, y, depth, start_x, start_y):
    visited[x][y] = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if not visited[nx][ny] and arr[nx][ny] == arr[x][y]:
                if dfs(nx, ny, depth+1, start_x, start_y):
                    return True
            elif visited[nx][ny] and (nx, ny) == (start_x, start_y) and depth >=3:
                return True
    visited[x][y] = False
    return False
n, m = map(int, input().split())
arr = []
visited = [[0]*m for _ in range(n)]
for _ in range(n):
    arr.append(list(map(str, input())))
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if dfs(i, j, 0, i, j):
                print('Yes')
                exit()
print('No')