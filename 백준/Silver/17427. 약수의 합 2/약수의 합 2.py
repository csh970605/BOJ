# problem statement : https://www.acmicpc.net/problem/17427
import sys
input = sys.stdin.readline

def get_sum(num):
    gnum = 0
    for i in range(1, num+1):
        gnum += (n//i) * i
    return gnum

n = int(input())

result =  get_sum(n)
print(result)