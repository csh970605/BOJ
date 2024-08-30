# problem statement : https://www.acmicpc.net/problem/9613
import sys
input = sys.stdin.readline
from math import gcd

t = int(input())

for _ in range(t):
    arr = list(map(int, input().split()))[1:]
    result = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            result += gcd(arr[i], arr[j])
    print(result)