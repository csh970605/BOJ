# problem statement : https://www.acmicpc.net/problem/1931
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x: (x[1], x[0]))
start_now = -1
end_now = -1
count = 0
for start, end in arr:
    if start >= end_now:
        start_now = start
        end_now = end
        count += 1
print(count)