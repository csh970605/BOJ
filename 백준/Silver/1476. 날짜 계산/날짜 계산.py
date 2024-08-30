# problem statement : https://www.acmicpc.net/problem/1476
import sys
input = sys.stdin.readline

e, s, m = map(int, input().split())

count = 0
a, b, c = 1, 1, 1
for i in range(1, 7981):
    if (a, b, c) == (e, s, m):
        print(i)
        exit()
    a += 1
    b += 1
    c += 1
    if a > 15:
        a = 1
    if b > 28 :
        b = 1
    if c > 19:
        c = 1