# problem statement : https://www.acmicpc.net/problem/13397
import sys
input = sys.stdin.readline
from collections import deque

def bfs(a, b, count):
    q = deque()
    q.append((a,count))
    while q:
        x, count = q.popleft()
        if x == b:
            return count
        for nx in (x*2, x*10+1):
            if nx <= b:
                q.append((nx, count+1))
    return -1
a, b = map(int, input().split())
print(bfs(a, b, 1))