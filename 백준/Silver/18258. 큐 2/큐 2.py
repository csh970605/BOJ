# problem statement : https://www.acmicpc.net/problem/18258

from collections import deque
import sys
que = deque()

n = int(input())
for _ in range(n):
    s = list(map(str, sys.stdin.readline().split()))
    if s[0] == 'push':
        que.append(int(s[1]))
    elif s[0] == 'front':
        if len(que):
            print(que[0])
        else:
            print(-1)
    elif s[0] == 'pop':
        if len(que):
            print(que.popleft())
        else:
            print(-1)
    elif s[0] == 'size':
        print(len(que))
    elif s[0] == 'empty':
        if len(que):
            print(0)
        else:
            print(1)
    elif s[0] == 'back':
        if len(que):
            print(que[-1])
        else:
            print(-1)