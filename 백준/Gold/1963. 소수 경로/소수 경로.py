# problem statement : https://www.acmicpc.net/problem/1963
import sys
input = sys.stdin.readline
from collections import deque

def bfs(start, target, primes):
    q = deque([(start, 0)])
    visited = [0] * 10000
    visited[int(start)] = 1

    while q:
        x, count = q.popleft()
        if x == target:
            return count
        
        for i in range(4):
            for j in range(10):
                if i == 0 and j == 0:
                    continue
                nx = x[:i]+str(j)+x[i+1:]
                
                if not visited[int(nx)] and primes[int(nx)]:
                    visited[int(nx)] = 1
                    q.append((nx, count+1))
    
    return "Impossible" 

def sieve():
    primes = [1] * 10000
    primes[0] = primes[1] = 0
    for i in range(2, int(10000**0.5) + 1):
        if primes[i]:
            for j in range(i*i, 10000, i):
                primes[j] = 0
    return primes

primes = sieve()

t = int(input())
for _ in range(t):
    start, target = input().split()
    print(bfs(start, target, primes))