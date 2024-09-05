# problem statement : https://www.acmicpc.net/problem/14226
import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    q = deque()
    q.append((1, 0, 0))
    visited[1][0] = 1

    while q:
        num, time, clip_board = q.popleft()
        if num == n:
            return time
        if visited[num][num] == -1:
            visited[num][num] = time + 1
            q.append((num, time+1, num))

        if clip_board > 0 and num+clip_board <= n and visited[num+clip_board][clip_board] == -1:
            visited[num+clip_board][clip_board] = time + 1
            q.append((num+clip_board, time+1, clip_board))

        if num > 1 and visited[num-1][clip_board] == -1:
            visited[num-1][clip_board] = time + 1
            q.append((num-1, time+1, clip_board))

n = int(input())
visited = [[-1]*(n+1) for _ in range(n+1)]
print(bfs())