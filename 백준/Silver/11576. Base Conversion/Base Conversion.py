# problem statement : https://www.acmicpc.net/problem/11576
import sys
input = sys.stdin.readline

a, b = map(int, input().split())

m = int(input())
num = list(map(int, input().split()))
r10 = 0
for i, n in enumerate(num):
    if n == 0:
        r10 += 0
    else:
        r10 += n*a**(len(num)-i-1)

if r10 == 0:
    print(0)
else:
    result = []
    while r10 != 0:
        c = r10 // b
        d = r10 % b
        r10 //= b
        result.append(str(d))
    print(' '.join(result[::-1]))