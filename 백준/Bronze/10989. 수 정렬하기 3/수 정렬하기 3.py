# problem statement : https://www.acmicpc.net/problem/10989
import sys

n = int(sys.stdin.readline().rstrip())
arr = [0]*10001
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    arr[num] += 1

for i in range(10001):
    if arr[i] > 0:   
        for _ in range(arr[i]):
            sys.stdout.write(f'{i}\n')