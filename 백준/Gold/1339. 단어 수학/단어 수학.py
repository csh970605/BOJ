# problem statement : https://www.acmicpc.net/problem/14888
import sys
input = sys.stdin.readline

n = int(input())
words = [input().strip() for _ in range(n)]

alphabet_weight = [0] * 26

for word in words:
    length = len(word)
    for i, char in enumerate(word):
        alphabet_weight[ord(char) - ord('A')] += 10 ** (length-i-1)

alphabet_weight.sort(reverse=True)

result = 0
num = 9
for weight in alphabet_weight:
    if weight == 0:
        break
    result += weight * num
    num -= 1

print(result)
