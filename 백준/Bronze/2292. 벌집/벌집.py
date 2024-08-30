# problem statement : https://www.acmicpc.net/problem/2292

n = int(input())

a = 1
i = 0
while True:
    if n == 1:
        print(1)
        break
    else:
        if a < n and n <= a + 6 * i:
            print(i+1)
            break
        a += 6 * i
        i += 1