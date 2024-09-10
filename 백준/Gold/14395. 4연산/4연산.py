# problem statement : https://www.acmicpc.net/problem/14395
import sys
input = sys.stdin.readline
from collections import deque

def bfs(start, operators):
    q = deque()
    q.append((start, operators))
    while q:
        x, operators = q.popleft()
        if x == target:
            return operators
        for op in '*+-/':
            if op == '*':
                nx = x * x
            elif op == '+':
                nx = x + x
            elif op == '-':
                nx = x - x
            else:
                nx = int(x / x)
            if nx not in visited and 0<nx<=start*target:
                q.append((nx, operators+op))
                visited.add(nx)
    return -1
start, target = map(int, input().split())
if start == target:
    print(0)
    exit()
visited = set()
visited.add(start)
print(bfs(start, ''))