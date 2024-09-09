# problem statement : https://www.acmicpc.net/problem/16928
import sys
input = sys.stdin.readline
from collections import deque
def bfs(x, count):
    q = deque()
    q.append((x, count))
    visited[x] = 1
    while q:
        x, count = q.popleft()
        for i in range(1, 7):
            nx = x + i
            if nx == 100:
                return count + 1
            if not visited[nx]:
                if nx in ladder:
                    nx = ladder[nx]
                    q.append((nx, count+1))
                    visited[nx] = 1
                elif nx in snake:
                    nx = snake[nx]
                    q.append((nx, count+1))
                    visited[nx] = 1
                else:
                    q.append((nx, count+1))
                    visited[nx] = 1
    return -1
n, m = map(int, input().split())
game_board = [0]*100
visited = [0]*100
ladder = dict()
snake = dict()

for _ in range(n):
    a, b = map(int, input().split())
    ladder[a] = b
for _ in range(m):
    a, b = map(int, input().split())
    snake[a] = b
print(bfs(1, 0))