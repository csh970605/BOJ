# problem statement : https://www.acmicpc.net/problem/1966

import sys
input = sys.stdin.readline
from collections import deque
cases = int(input())

for _ in range(cases):
    q = deque()
    count = 0
    n, m = list(map(int, input().split()))
    docs = list(map(int, input().split()))
    docset = list(set(docs))
    docset.sort(reverse=True)
    for i in range(n):
        q.append([docs[i], i])
    while q:
        if q[0][0] == max(q)[0]:
            count += 1
            if q[0][1] == m:
                print(count)
                break
            else:
                q.popleft()
        else:
            q.rotate(-1)