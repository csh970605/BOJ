# problem statement : https://www.acmicpc.net/problem/18110

import sys
input = sys.stdin.readline
def round(n):
    if n - int(n) >= 0.5:
        return int(n) + 1
    else:
        return int(n)

n = int(input())
if n == 0:
    print(0)
else:
    k = round(n*0.15)
    arr = []
    for _ in range(n):
        arr.append(int(input()))

    arr.sort()
    if k:
        arr = arr[k:-k]
    print(int(round(sum(arr)/len(arr))))
    