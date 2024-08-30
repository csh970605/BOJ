# problem statement : https://www.acmicpc.net/problem/2164

from collections import deque

q = deque()

n = int(input())

for i in range(1, n+1):
    q.append(i)
while len(q) > 1:
    q.popleft()
    a = q.popleft()
    q.append(a)
print(q.pop())