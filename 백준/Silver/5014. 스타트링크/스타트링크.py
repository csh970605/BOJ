# problem statement : https://www.acmicpc.net/problem/5014
import sys
input = sys.stdin.readline
from collections import deque

def bfs(f, s, g, u, d):
    q = deque()
    visited = [0] * (f+1)
    visited[s] = 1
    time = 0
    q.append((s, time))
    while q:
        pos, time = q.popleft()
        if pos == g:
            return time
        else:
            for np in (pos+u, pos-d):
                if 1<=np<(f+1) and visited[np] == 0:
                    visited[np] = 1
                    q.append((np, time+1))
    return 'use the stairs'

f, s, g, u, d = map(int, input().split())

if s < g and u <= 0:
    print('use the stairs')
elif s > g and d <= 0:
    print('use the stairs')
elif s == g:
    if u == 0 and d == 0:
        print('use the stairs')
    else:
        print(0)
else:
    print(bfs(f, s, g, u, d))