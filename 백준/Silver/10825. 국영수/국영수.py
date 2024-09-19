# problem statement : https://www.acmicpc.net/problem/10825
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(str, input().split())))
arr.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for line in arr:
    print(line[0])