# problem statement : https://www.acmicpc.net/problem/1748
import sys
input = sys.stdin.readline

n = int(input())
n_len = len(str(n))
arr = [9, 90, 900, 9000, 90000, 900000, 9000000, 90000000, 90000000]
result = 0
for i in range(1, n_len):
    result += i*arr[i-1]
num = '1'
for i in range(1, n_len):
    num += '0'
num_len = len(num)
result += (n-int(num)+1)*num_len
print(result)