# problem statement : https://www.acmicpc.net/problem/16946
import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y, group_num):
    q = deque()
    q.append((x, y))
    visited[x][y] = group_num
    count = 1 
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and not arr[nx][ny]:
                visited[nx][ny] = group_num
                q.append((nx, ny))
                count += 1
    return count

n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[0]*m for _ in range(n)]
group_size = dict()
group_num = 1

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 and not visited[i][j]:
            group_size[group_num] = bfs(i, j, group_num)
            group_num += 1


result = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            adjacent_groups = set() 
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if 0<=ni<n and 0<=nj<m and not arr[ni][nj]:
                    adjacent_groups.add(visited[ni][nj])
            
            total_size = 1 
            for group in adjacent_groups:
                total_size += group_size[group]
            
            result[i][j] = total_size % 10
        else:
            result[i][j] = 0

for row in result:
    print("".join(map(str, row)))