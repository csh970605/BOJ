# problem statement : https://www.acmicpc.net/problem/2501

try:
    n, k = list(map(int, input().split()))
    divisor = []
    index = 0
    for i in range(1, n+1):
        if n % i == 0:
            divisor.append(i)

    print(divisor[k-1])

except IndexError:
    print(0)