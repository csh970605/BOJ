# problem statement : https://www.acmicpc.net/problem/13549
import sys
input = sys.stdin.readline
from collections import deque

def bfs(n, k):
    q = deque()
    max_pos = 100001
    visited = [0]*max_pos
    time = 0
    q.append((n, time))

    while q:
        pos, time = q.popleft()
        if pos == k:
            return time
        for i, npos in enumerate((pos*2, pos-1, pos+1)):
            if 0<=npos<max_pos and not visited[npos]:
                if i == 0:
                    q.appendleft((npos, time))
                else:
                    q.append((npos, time+1))
                visited[npos] = 1
                

n, k = map(int, input().split())
if n == k:
    print(0)
else:
    print(bfs(n, k))