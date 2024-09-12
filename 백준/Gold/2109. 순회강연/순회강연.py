# problem statement : https://www.acmicpc.net/problem/2109
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
arr.sort(reverse=True)

max_heap = []
result = 0
day_check = [False] * 10001

for p, d in arr:
    for i in range(d, 0, -1):
        if not day_check[i]:
            day_check[i] = True
            result += p
            break
print(result)
