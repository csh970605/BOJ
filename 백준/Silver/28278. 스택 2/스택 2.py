# problem statement : https://www.acmicpc.net/problem/28278
import sys
stack = []

n = int(input())

for _ in range(n):
    x = sys.stdin.readline().strip()
    if x[0] == '1':
        _, x = x.split()
        stack.append(int(x))
    elif x == '2':
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif x == '3':
        print(len(stack))
    elif x == '4':
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    elif x == '5':
        if len(stack)>0:
            print(stack[-1])
        else:
            print(-1)