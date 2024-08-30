# problem statement : https://www.acmicpc.net/problem/1259

import sys
input = sys.stdin.readline

while True:
    check = True
    n = input().strip()
    length = len(n)
    if n == '0':
        break
    for i in range(length//2):
        if n[i] != n[length-i-1]:
            check = False
            print('no')
            break
    if check:
        print('yes')