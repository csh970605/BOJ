# problem statement : https://www.acmicpc.net/problem/10799
import sys
input = sys.stdin.readline
stack = []

string = input().strip()
count = 1
result = 0
check = False
for i in range(len(string)):
    if string[i] == '(':
        stack.append('(')
    else:
        if stack:
            stack.pop()
            if string[i-1] == '(':
                result += len(stack)
            else:
                result += 1
        else:
            print('error')
print(result)