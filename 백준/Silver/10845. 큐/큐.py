# problem statement : https://www.acmicpc.net/problem/10845

import sys
input = sys.stdin.readline
from collections import deque

q = deque()
n = int(input())
for _ in range(n):
    command = list(map(str, input().split()))
    if command[0] == 'push':
        q.append(command[1])
    elif command[0] == 'pop':
        if len(q):
            print(q.popleft())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(q))
    elif command[0] == 'empty':
        if len(q):
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if len(q):
            print(q[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if len(q):
            print(q[-1])
        else:
            print(-1)