# problem statement : https://www.acmicpc.net/problem/10973
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

index = n - 1
index2 = n-1
while index > 0 and arr[index-1] <= arr[index]:
    index -= 1

if index == 0:
    print(-1)
    exit()

while arr[index-1] <= arr[index2]:
    index2 -= 1
arr[index-1], arr[index2] = arr[index2], arr[index-1]

arr[index:] = reversed(arr[index:])
print(' '.join(map(str, arr)))
