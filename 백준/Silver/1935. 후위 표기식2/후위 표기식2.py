# problem statement : https://www.acmicpc.net/problem/1935
import sys
input = sys.stdin.readline

n = int(input())
postfix = input().strip()
alph_dict = {}
for i in range(n):
    alph_dict[chr(65+i)] = int(input())
stack = []
for char in postfix:
    if 'A' <= char <= 'Z':
        stack.append(alph_dict[char])
    else:
        b = stack.pop()
        a = stack.pop()
        if char == '+':
            stack.append(a+b)
        elif char == '-':
            stack.append(a-b)
        elif char == '*':
            stack.append(a*b)
        elif char == '/':
            stack.append(a/b)
print(f'{stack[0]:.2f}')
    