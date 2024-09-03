# problem statement : https://www.acmicpc.net/problem/10974
import sys
input = sys.stdin.readline
import math
n = int(input())
arr = [i for i in range(1, n+1)]
print(' '.join(map(str, arr)))

for _ in range(math.factorial(n)-1):
    index1 = n - 2
    index2 = n - 1
    while index1 >= 0 and arr[index1] >= arr[index1+1]:
        index1 -= 1

    while arr[index1] >= arr[index2]:
        index2 -= 1

    arr[index1], arr[index2] = arr[index2], arr[index1]

    arr[index1+1:] = reversed(arr[index1+1:])
    print(' '.join(map(str, arr)))