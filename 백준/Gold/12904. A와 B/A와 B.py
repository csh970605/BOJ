# problem statement : https://www.acmicpc.net/problem/12904
import sys
input = sys.stdin.readline


s = input().strip()
t = input().strip()

while len(t) > len(s):
    if t[-1] == 'A':
        t = t[:-1]
    elif t[-1] == 'B':
        t = t[:-1][::-1]

if t == s:
    print(1)
else:
    print(0)