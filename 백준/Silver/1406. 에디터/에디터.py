# problem statement : https://www.acmicpc.net/problem/1406

import sys
input = sys.stdin.readline

left = list(map(str, input().strip()))
right = []
n = int(input())
for _ in range(n):
    command = list(map(str, input().split()))
    if command[0] == 'L':
        if left:
            right.append(left.pop())
    elif command[0] == 'D':
        if right:
            left.append(right.pop())
    elif command[0] == 'B':
        if left:
            left.pop()
    elif command[0] == 'P':
        left.append(command[1])
print(''.join(left+right[::-1]))