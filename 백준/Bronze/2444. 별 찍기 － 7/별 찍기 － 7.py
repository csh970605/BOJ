# problem statement : https://www.acmicpc.net/problem/11718

n = int(input())

for i in range(1, n+1):
    print(' '*(n-i)+'*'*(2*i-1))

for i in range(n-1, 0, -1):
    print(' '*(n-i)+'*'*(2*i-1))
    