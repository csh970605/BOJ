# problem statement : https://www.acmicpc.net/problem/11656
import sys
input = sys.stdin.readline

string = input().strip()
arr = []
for i in range(len(string)):
    arr.append(string[i:])
arr.sort()
print('\n'.join(arr))