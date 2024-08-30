# problem statement : https://www.acmicpc.net/problem/2501

while True:
    n = int(input())
    if n == -1:
        break
    divisors = []
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
            sum += i

    if sum == n:
        print(f'{n} = ', end='')
        print(' + '.join(map(str, divisors)))
    else:
        print(f'{n} is NOT perfect.')
    