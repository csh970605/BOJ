# problem statement : https://www.acmicpc.net/problem/2609

import sys
input = sys.stdin.readline
import math

a, b = list(map(int, input().split()))
print(math.gcd(a,b))
print(math.lcm(a,b))