# problem statement : https://www.acmicpc.net/problem/1676

import sys
input = sys.stdin.readline
import math

n = int(input())
fac = str(math.factorial(n))
count = 0
index = -1
while True:
    n = fac[index]
    if n == '0':
        count+=1
        index -= 1
    else:
        break
print(count)