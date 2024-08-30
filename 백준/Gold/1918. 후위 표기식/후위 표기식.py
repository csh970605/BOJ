# problem statement : https://www.acmicpc.net/problem/1918
import sys
input = sys.stdin.readline

infix = input().strip()
output_stack = []
temp_stack = []
for char in infix:
    if 'A' <= char <= 'Z':
        output_stack.append(char)
    elif char in ('*', '/'):
        while temp_stack and temp_stack[-1] not in ('+', '-', '('):
            output_stack.append(temp_stack.pop())
        temp_stack.append(char)
        
    elif char == '(':
        temp_stack.append(char)
    elif char == ')':
        while temp_stack and temp_stack[-1] != '(':
            output_stack.append(temp_stack.pop())
        temp_stack.pop()
    elif char in ('+', '-'):
        while temp_stack and temp_stack[-1] != '(':
            output_stack.append(temp_stack.pop())
        temp_stack.append(char)

while temp_stack:
    output_stack.append(temp_stack.pop())
    

print(''.join(output_stack))