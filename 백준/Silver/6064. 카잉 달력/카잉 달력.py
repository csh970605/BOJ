# problem statement : https://www.acmicpc.net/problem/6064
import sys
input = sys.stdin.readline
import math

t = int(input())

for _ in range(t):
    m, n, x, y = map(int, input().split())
    check = True
    while x <= m*n:
        if (x-y)%n == 0:
            print(x)
            check = False
            break
        x += m
    if check:
        print(-1)