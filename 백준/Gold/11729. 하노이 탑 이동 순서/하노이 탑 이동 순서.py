# problem statement : https://www.acmicpc.net/problem/11729
import sys
input = sys.stdin.readline

def hanoi(n, start, end, next):
    if n == 1:
        print(start, end)
    else:
        hanoi(n - 1, start, next, end)
        print(start, end)
        hanoi(n - 1, next, end, start)

n = int(input())
print(2**n-1)
hanoi(n, 1, 3, 2)