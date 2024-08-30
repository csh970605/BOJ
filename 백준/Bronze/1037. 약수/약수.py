# problem statement : https://www.acmicpc.net/problem/1307
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
if len(arr) < 2:
    print(arr[0]**2)
else:
    print(arr[0]*arr[-1])