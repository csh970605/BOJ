# problem statement : https://www.acmicpc.net/problem/4153
import sys

while True:
    a = list(map(int, sys.stdin.readline().split()))
    if a == [0, 0, 0]:
        break
    a.sort()
    if int(a[2]**2) == int(a[1]**2+a[0]**2):
        print('right')
    else:
        print('wrong')