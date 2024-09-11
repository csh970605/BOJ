# problem statement : https://www.acmicpc.net/problem/1541
import sys
input = sys.stdin.readline

command = input().strip()

subtraction_split = command.split('-')

result = sum(map(int, subtraction_split[0].split('+')))

for part in subtraction_split[1:]:
    result -= sum(map(int, part.split('+')))

print(result)