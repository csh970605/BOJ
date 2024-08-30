# problem statement : https://www.acmicpc.net/problem/1012
import sys
input = sys.stdin.readline
from collections import deque
def bfs(n, k):
    max_position = 100001
    visited = [0]*max_position
    # q = [[x, y]]
    q = deque([(n, 0)])
    while q:
        position, time = q.popleft()
        if position == k:
            return time
        for np in(position-1, position+1, position*2):
            if 0 <= np < max_position and visited[np] == 0:
                visited[np] = 1
                q.append((np, time+1))
n, k = map(int, input().split())
count = bfs(n, k)
print(count)