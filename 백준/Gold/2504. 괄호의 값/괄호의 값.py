# problem statement : https://www.acmicpc.net/problem/2504
import sys
input = sys.stdin.readline

string = input().strip()
stack = []
for i in range(len(string)):

    if string[i] in ('(', '['):
        stack.append(string[i])
    else:
        if not stack:
            break
        if string[i] == ')':
            if stack[-1] == '(':
                stack.pop()
                stack.append(2)
            else:
                temp = 0
                while stack and isinstance(stack[-1], int):
                    temp += stack.pop()
                if stack and stack[-1] == '(':
                    stack.pop()
                    stack.append(temp*2)
                else:
                    break
        elif string[i] == ']':
            if stack[-1] == '[':
                stack.pop()
                stack.append(3)
            else:
                temp = 0
                while stack and isinstance(stack[-1], int):
                    temp += stack.pop()
                if stack and stack[-1] == '[':
                    stack.pop()
                    stack.append(temp*3)
                else:
                    break

try:
    result = 0
    for i in stack:
        if isinstance(i, int):
            result += i
        else:
            result = 0
            break
    print(result)
except BaseException:
    print(0)
