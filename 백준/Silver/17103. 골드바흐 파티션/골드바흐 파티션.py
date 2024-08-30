# problem statement : https://www.acmicpc.net/problem/17103

import math
def sieve_eratos(limit):
    sieve = [1] * (limit+1)
    sieve[0] = sieve[1] == 0
    for n in range(2, int(math.sqrt(limit))+1):
        if sieve[n]:
            for m in range(n**2, limit+1, n):
                sieve[m] = False
    sieve[0] = sieve[1] == 0
    return sieve

limit = 1000000
sieve = sieve_eratos(limit)
n = int(input())

for _ in range(n):
    m = int(input().strip())
    count = 0
    for i in range(2, int(m/2+1)):
        if sieve[i] and sieve[m-i]:
            count += 1
    print(count)