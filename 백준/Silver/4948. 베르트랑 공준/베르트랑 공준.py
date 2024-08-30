# problem statement : https://www.acmicpc.net/problem/4948
import math
arr = []

while True:
    n = int(input())
    if n == 0:
        break
    arr.append(n)
    

countarr = [1]*((123456)*2+1)
countarr[0] = countarr[1] == 0
for num in range(2, int(math.sqrt(123456*2))+1):
    if countarr[num]:
        for n in range(num*num, 123456*2+1, num):
            countarr[n] = 0
for m in arr:
    print(sum(countarr[m+1:2*m+1]))
