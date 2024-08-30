# problem statement : https://www.acmicpc.net/problem/13913
import sys
input = sys.stdin.readline
from collections import deque

def bfs(n, k):
    q = deque()
    max_pos = 100001
    visited = [-1]*max_pos
    time = 0
    q.append((n, time))

    while q:
        pos, time = q.popleft()
        if pos == k:
            path = []
            while pos != n:
                path.append(pos)
                pos = visited[pos]
            path.append(n)
            path.reverse()
            print(time)
            print(' '.join(map(str, path)))
        for npos in (pos-1, pos+1, pos*2):
            if 0<=npos<max_pos and visited[npos] == -1:
                q.append((npos, time+1))
                visited[npos] = pos
                

n, k = map(int, input().split())
if n == k:
    print(0)
    print(n)
else:
    bfs(n, k)