# problem statement : https://www.acmicpc.net/problem/6603
import sys
input = sys.stdin.readline
from itertools import permutations

while True:
    arr = list(map(int, input().split()))
    n = arr[0]
    if n == 0:
        break
    arr = arr[1:]
    for per in permutations(arr, 6):
        if per[0] < per[1] < per[2] < per[3] < per[4] < per[5]:
            print(' '.join(map(str, per)))
    print()
    