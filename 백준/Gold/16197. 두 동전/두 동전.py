# problem statement : https://www.acmicpc.net/problem/16197
import sys
input = sys.stdin.readline
from collections import deque

def bfs(coin_1, coin_2):
    q = deque()
    q.append((coin_1[0], coin_1[1], coin_2[0], coin_2[1], 0))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        x1, y1, x2, y2, count = q.popleft()
        if count > 10:
            return -1
        if (x1 < 0 or x1 >= n or y1 < 0 or y1 >= m) and (0 <= x2 < n and 0 <= y2 < m):
            return count
        if (x2 < 0 or x2 >= n or y2 < 0 or y2 >= m) and (0 <= x1 < n and 0 <= y1 < m):
            return count
        if (x1 < 0 or x1 >= n or y1 < 0 or y1 >= m) and (x2 < 0 or x2 >= n or y2 < 0 or y2 >= m):
            continue

        for i in range(4):
            nx1 = x1 + dx[i]
            ny1 = y1 + dy[i]
            nx2 = x2 + dx[i]
            ny2 = y2 + dy[i]
            if 0 <= nx1 < n and 0 <= ny1 < m and arr[nx1][ny1] == '#':
                nx1, ny1 = x1, y1
            if 0 <= nx2 < n and 0 <= ny2 < m and arr[nx2][ny2] == '#':
                nx2, ny2 = x2, y2
            if (nx1, ny1, nx2, ny2) not in visited:
                visited.add((nx1, ny1, nx2, ny2))
                q.append((nx1, ny1, nx2, ny2, count+1))
    return -1
n, m = map(int, input().split())
arr = []
check = True
for i in range(n):
    arr.append(list(map(str, input().strip())))
    for j, char in enumerate(arr[i]):
        if char == 'o':
            if check:
                coin_1 = [i, j]
                check = False
            else:
                coin_2 = [i, j]
visited = set()
visited.add((coin_1[0], coin_1[1], coin_2[0], coin_2[1]))
print(bfs(coin_1, coin_2))