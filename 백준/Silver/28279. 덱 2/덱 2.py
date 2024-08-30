# problem statement : https://www.acmicpc.net/problem/28279
from collections import deque
import sys

n = int(input())
q = deque()
for _ in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    if a[0] == 1:
        q.appendleft(a[1])
    elif a[0] == 2:
        q.append(a[1])
    elif a[0] == 3:
        if len(q):
            print(q.popleft())
        else:
            print(-1)
    elif a[0] == 4:
        if len(q):
            print(q.pop())
        else:
            print(-1)
    elif a[0] == 5:
        print(len(q))
    elif a[0] == 6:
        if len(q):
            print(0)
        else:
            print(1)
    elif a[0] == 7:
        if len(q):
            print(q[0])
        else:
            print(-1)
    elif a[0] == 8:
        if len(q):
            print(q[-1])
        else:
            print(-1)