# problem statement : https://www.acmicpc.net/problem/11728
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
i, j = 0, 0
result = []

while i < n and j < m:
    if arr1[i] <= arr2[j]:
        result.append(arr1[i])
        i += 1
    else:
        result.append(arr2[j])
        j += 1

if i < n:
    result.extend(arr1[i:])
if j < m:
    result.extend(arr2[j:])

print(' '.join(map(str, result)))