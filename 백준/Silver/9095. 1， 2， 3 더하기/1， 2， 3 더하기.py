# problem statement : https://www.acmicpc.net/problem/9095
import sys
input = sys.stdin.readline
from math import factorial


t = int(input())
for _ in range(t):
    n = int(input())
    count = 0


    for i in range(n//3+1):  
        temp1 = n - 3*i 
        if temp1 == 0:
            count += (int(factorial((i))/(factorial(i))))
            continue
        
        for j in range(temp1//2+1):
            temp2 = temp1 - 2*j 
            if temp2 == 0:
                count += (int(factorial((i+j))/(factorial(i)*factorial(j))))
                continue
            
            for k in range(temp2+1): 
                if temp2 == k:
                    count += (int(factorial((i+j+k))/(factorial(i)*factorial(j)*factorial(k))))

    print(count)
