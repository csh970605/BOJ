# problem statement : https://www.acmicpc.net/problem/1744
import sys
input = sys.stdin.readline

n = int(input())
positives = []
negatives = []
ones = 0
zero = False

for _ in range(n):
    num = int(input())
    if num > 1:
        positives.append(num)
    elif num == 1:
        ones += 1
    elif num == 0:
        zero = True
    else:
        negatives.append(num)

positives.sort(reverse=True)
negatives.sort()

result = 0
for i in range(0, len(positives) - 1, 2):
    result += positives[i] * positives[i + 1]
if len(positives) % 2 == 1:
    result += positives[-1]

for i in range(0, len(negatives) - 1, 2):
    result += negatives[i] * negatives[i + 1]
if len(negatives) % 2 == 1:
    if not zero:
        result += negatives[-1]

result += ones

print(result)