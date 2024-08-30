# problem statement : https://www.acmicpc.net/problem/2309
import sys
input = sys.stdin.readline

arr = []
for _ in range(9):
    arr.append(int(input()))
arr.sort()

for i in range(8): 
    for j in range(i+1, 9):
        if sum(arr[:i]) + sum(arr[i+1:j]) + sum(arr[j+1:]) == 100:
            print('\n'.join([str(arr[k]) for k in range(9) if k != i and k != j]))
            exit()
