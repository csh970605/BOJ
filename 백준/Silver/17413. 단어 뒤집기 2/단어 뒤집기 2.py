# problem statement : https://www.acmicpc.net/problem/17413
import sys
input = sys.stdin.readline

words = input().strip()
check = False
stack = []
for char in words:
    
    if char == '<':
        check = True
        while stack:
            print(stack.pop(), end='')
        print('<', end='')
    elif char == '>':
        check = False
        print('>', end='')
    if char == ' ':
        while stack:
            print(stack.pop(), end='')
        print(' ', end='')
    if check and char not in ('<', '>', ' '):
        print(char, end='')
    elif not check and char not in ('<', '>', ' '):
        stack.append(char)
while stack:
    print(stack.pop(), end='')
print(' ', end='')