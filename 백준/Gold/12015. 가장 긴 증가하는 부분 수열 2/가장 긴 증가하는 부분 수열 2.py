# problem statement : https://www.acmicpc.net/problem/12015
import sys
input = sys.stdin.readline
import bisect

n = int(input())
arr = list(map(int, input().split()))

lis = []

for num in arr:
    pos = bisect.bisect_left(lis, num)
    if pos == len(lis):
        lis.append(num)
    else:
        lis[pos] = num
print(len(lis))