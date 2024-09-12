# problem statement : https://www.acmicpc.net/problem/12919
import sys
input = sys.stdin.readline

def check(s, t):
    if len(s) == len(t):
        return s == t
    
    if t[-1] == 'A':
        if check(s, t[:-1]):
            return True
    
    if t[0] == 'B':
        if check(s, t[:0:-1]):
            return True
    
    return False

s = input().strip()
t = input().strip()

if check(s, t):
    print(1)
else:
    print(0)