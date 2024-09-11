# problem statement : https://www.acmicpc.net/problem/1783
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

if n == 1:
    print(1)

elif n == 2:
    print(min(4, (m + 1) // 2))

else:
    if m < 7:
        print(min(4, m))
    else:
        print(m - 2)
