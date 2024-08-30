# problem statement : https://www.acmicpc.net/problem/2346
from collections import deque
n = int(input())
arr = list(map(int, input().strip().split()))
q = deque((i+1, arr[i]) for i in range(n))
result = []

while q:
    index, num = q.popleft()
    result.append(index)
    if not q:
        break
    if num > 0:
        q.rotate(-(num-1))
    else:
        q.rotate(-num)
print(' '.join([str(x) for x in result]))