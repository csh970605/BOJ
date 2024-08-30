# problem statement : https://www.acmicpc.net/problem/2004
import sys
input = sys.stdin.readline
import math

def count_nums(n, num):
    count = 0
    while n >= num:
        n //= num
        count += n
    return count
n, m = map(int, input().split())

count2 = count_nums(n, 2) - count_nums(m, 2) - count_nums(n-m, 2)
count5 = count_nums(n, 5) - count_nums(m, 5) - count_nums(n-m, 5)
print(min(count2, count5))