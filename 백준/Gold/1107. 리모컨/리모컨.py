# problem statement : https://www.acmicpc.net/problem/1107
import sys
input = sys.stdin.readline
from collections import deque

def find_min(n, brokens):
    min_c = abs(n-100)
    for i in range(1000000):
        check = False
        count = 0
        for j in str(i):
            if j in brokens:
                check = True
        if not check:
            count = len(str(i)) + abs(i-n)
            if count < min_c:
                min_c = count
    return min_c
    
n = int(input())
broken = int(input())
if broken > 0:
    brokens = set(input().strip().split())
else:
    brokens = set()
    
if n == 100:
    print(0)
else:
    print(find_min(n, brokens))