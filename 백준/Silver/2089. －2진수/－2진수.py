# problem statement : https://www.acmicpc.net/problem/2089
import sys
input = sys.stdin.readline

n = int(input())

if n == 0:
    print(0)
else:
    result = ''
    while n != 0:
        a = n // -2
        b = n % -2
        n //= -2
        if b < 0:
            b += 2
            n += 1
        result += str(b)
    print(result[::-1])