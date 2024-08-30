# problem statement : https://www.acmicpc.net/problem/1934

import math

n = int(input())
arr = []

for _ in range(n):
    a, b = map(int, input().split())
    gcd = math.gcd(a, b)
    lcm = (a * b) // gcd
    arr.append(lcm)

for num in arr:
    print(int(num))
