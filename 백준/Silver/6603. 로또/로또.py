# problem statement : https://www.acmicpc.net/problem/6603
import sys
input = sys.stdin.readline
from itertools import combinations

while True:
    arr = list(map(int, input().split()))
    n = arr[0]
    if n == 0:
        break
    arr = arr[1:]
    for comb in combinations(arr, 6):
        print(' '.join(map(str, comb)))
    print()
    