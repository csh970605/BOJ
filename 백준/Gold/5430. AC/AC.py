# problem statement : https://www.acmicpc.net/problem/5430
import sys
input = sys.stdin.readline
from collections import deque

t = int(input())

for _ in range(t):
    command = input().strip()
    n = int(input().strip())
    q = input().strip()[1:-1].split(',')

    if n == 0:
        q = deque()
    else:
        q = deque(q)

    reverse = False
    error = False

    for c in command:
        if c == 'R':
            reverse = not reverse
        elif c == 'D':
            if not q:
                print('error')
                error = True
                break
            if reverse:
                q.pop()
            else:
                q.popleft()

    if not error:
        if reverse:
            q.reverse()
        print('[' + ','.join(q) + ']')