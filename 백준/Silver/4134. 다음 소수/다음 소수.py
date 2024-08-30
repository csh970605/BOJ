# problem statement : https://www.acmicpc.net/problem/4134
import math
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
for m in arr:
    if m == 0 or m == 1 or m == 2:
        print(2)
    else:
        for i in range(m, m*2):
            check = True
            for j in range(2, int(math.sqrt(i)+1)):
                if i % j == 0:
                    check = False
                    break
            if check:
                print(i)
                break
