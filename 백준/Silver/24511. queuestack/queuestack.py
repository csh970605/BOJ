# problem statement : https://www.acmicpc.net/problem/24511

from collections import deque
import sys

n = int(sys.stdin.readline())
dss = list(map(int, sys.stdin.readline().split()))
rot = sum(dss)
nums = list(map(int, sys.stdin.readline().split()))
result = []
q = deque()
for i in range(n):
    if dss[i] == 0:
        q.append(nums[i])
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

for num in nums:
    q.append(num)
    q.rotate(2)
    result.append(q.popleft())

print(' '.join(str(x) for x in result))