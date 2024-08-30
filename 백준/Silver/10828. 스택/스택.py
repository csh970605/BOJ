# problem statement : https://www.acmicpc.net/problem/10828

import sys
input = sys.stdin.readline

stack = []
n = int(input())
for _ in range(n):
    command = list(map(str, input().split()))
    if command[0] == 'push':
        stack.append(int(command[1]))
    elif command[0] == 'pop':
        if len(stack):
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack):
            print(0)
        else:
            print(1)
    elif command[0] == 'top':
        if len(stack):
            print(stack[-1])
        else:
            print(-1)