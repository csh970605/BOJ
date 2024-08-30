# problem statement : https://www.acmicpc.net/problem/1158
import sys
input = sys.stdin.readline
from collections import deque
n, k = list(map(int, input().split()))
arr = [i for i in range(1, n+1)]
q = deque(arr)
result = []
while q:
    q.rotate(-k+1)
    result.append(str(q.popleft()))
print('<'+ ', '.join(result) + '>')