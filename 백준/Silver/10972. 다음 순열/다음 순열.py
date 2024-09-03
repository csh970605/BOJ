# problem statement : https://www.acmicpc.net/problem/15666
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr_len = len(arr)
index = arr_len - 2
check = True
while index >= 0 and arr[index] >= arr[index+1]:
    index -= 1

if index == -1:
    check = False
    print(-1)
    exit()

index2 = arr_len - 1
while arr[index] >= arr[index2]:
    index2 -= 1

arr[index], arr[index2] = arr[index2], arr[index]

arr[index+1:] = reversed(arr[index+1:])
if check:
    print(' '.join(map(str, arr)))
