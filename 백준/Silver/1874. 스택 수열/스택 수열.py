# problem statement : https://www.acmicpc.net/problem/1874
import sys
input = sys.stdin.readline
arr = []
n = int(input())
last = 1
result = []
input_string = []
for _ in range(n):
    input_string.append(int(input()))
try:
    for m in input_string:
        while last <= m:
            arr.append(last)
            result.append('+')
            last += 1
        if arr[-1] == m:
            arr.pop()
            result.append('-')
        else:
            break
    if arr:
        print('NO')
    else:
        print('\n'.join(result))
except IndexError:
    print('NO')