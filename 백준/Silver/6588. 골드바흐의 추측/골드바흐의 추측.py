# problem statement : https://www.acmicpc.net/problem/6588
import sys
input = sys.stdin.readline
import math
def sieve_eratos(limit):
    sieve = [1] * (limit+1)
    sieve[0] = sieve[1] == 0
    for n in range(2, int(math.sqrt(limit))+1):
        if sieve[n]:
            for m in range(n**2, limit+1, n):
                sieve[m] = 0
    return sieve

arr = sieve_eratos(1000000)

while True:
    n = int(input())
    if n == 0:
        break
    check = False
    for i in range(3, n-2, 2):
        if arr[i] and arr[n-i]:
            print(f'{n} = {i} + {n-i}')
            break
    else:
        print("Goldbach's conjecture is wrong.")
