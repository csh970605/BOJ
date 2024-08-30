# problem statement : https://www.acmicpc.net/problem/1475
import sys
input = sys.stdin.readline

arr = [0]*9

ns = input().strip()

for n in ns:
    n = int(n)
    if n == 9:
        n = 6
    arr[n] += 1
if arr[6] % 2 == 1:
    arr[6] = arr[6] // 2 + 1
else:
    arr[6] = arr[6] // 2
print(max(arr))