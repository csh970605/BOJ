# problem statement : https://www.acmicpc.net/problem/14888
import sys
input = sys.stdin.readline
from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))
nums = list(map(int, input().split()))
operators = []
for i, num in enumerate(nums):
    for j in range(num):
        if i == 0:
            operators.append('+')
        elif i == 1:
            operators.append('-')
        elif i == 2:
            operators.append('*')
        elif i == 3:
            operators.append('/')
operator_permutations = set(permutations(operators))

max_value = -float('inf')
min_value = float('inf')

for operator_seq in operator_permutations:
    result = arr[0]
    for i in range(1, n):
        if operator_seq[i-1] == '+':
            result += arr[i]
        elif operator_seq[i-1] == '-':
            result -= arr[i]
        elif operator_seq[i-1] == '*':
            result *= arr[i]
        elif operator_seq[i-1] == '/':
            if result < 0:
                result = -(-result // arr[i])
            else:
                result //= arr[i]
    
    max_value = max(max_value, result)
    min_value = min(min_value, result)

print(max_value)
print(min_value)