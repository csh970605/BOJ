# problem statement : https://www.acmicpc.net/problem/5397
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    left = []
    right = []
    string = input().strip()

    for s in string:
        if s == '>':
            if right:
                left.append(right.pop())
        elif s == '<':
            if left:
                right.append(left.pop())
        elif s == '-':
            if left:
                left.pop()
        else:
            left.append(s)
    print(''.join(left+right[::-1]))