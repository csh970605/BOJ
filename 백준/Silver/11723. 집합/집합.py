# problem statement : https://www.acmicpc.net/problem/11723
import sys
input = sys.stdin.readline

n = int(input())
s = set()
for _ in range(n):
    command = list(map(str, input().split()))
    if command[0] == 'add':
        s.add(int(command[1]))

    elif command[0] == 'remove':
        s.discard(int(command[1]))

    elif command[0] == 'check':
        if int(command[1]) in s:
            print(1)
        else:
            print(0)
    elif command[0] == 'toggle':
        num = int(command[1])
        if num in s:
            s.discard(num)
        else:
            s.add(num)
    elif command[0] == 'all':
        s = set(range(1, 21))
    elif command[0] == 'empty':
        s = set()