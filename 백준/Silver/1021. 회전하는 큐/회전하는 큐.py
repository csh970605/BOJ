# problem statement : https://www.acmicpc.net/problem/1021
import sys
input = sys.stdin.readline
from collections import deque
n, m = list(map(int, input().split()))
q = [i for i in range(1, n+1)]
q = deque(q)
arr = list(map(int,input().split()))
result = 0
result1 = 0
result2 = 0
for num in arr:
    q1 = q.copy()
    q2 = q.copy()
    result1 = result
    result2 = result
    while True:
        if q1[0] == num:
            q1.popleft()
            break
        else:
            q1.rotate(1)
            result1 += 1
    while True:
        if q2[0] == num:
            q2.popleft()
            break
        else:
            q2.rotate(-1)
            result2 += 1
    if result1 > result2:
        q = q2
        result = result2
    else:
        q = q1
        result = result1
print(result)