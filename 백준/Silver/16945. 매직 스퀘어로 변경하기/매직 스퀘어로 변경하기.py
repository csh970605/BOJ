# problem statement : https://www.acmicpc.net/problem/16945
import sys
input = sys.stdin.readline

arr = []
for _ in range(3):
    arr.extend(list(map(int, input().split())))

magic_squares = [
    [8, 1, 6, 3, 5, 7, 4, 9, 2],
    [6, 1, 8, 7, 5, 3, 2, 9, 4],
    [4, 9, 2, 3, 5, 7, 8, 1, 6],
    [2, 9, 4, 7, 5, 3, 6, 1, 8],
    [8, 3, 4, 1, 5, 9, 6, 7, 2],
    [4, 3, 8, 9, 5, 1, 2, 7, 6],
    [6, 7, 2, 1, 5, 9, 8, 3, 4],
    [2, 7, 6, 9, 5, 1, 4, 3, 8]
]

min_value = float('inf')
for magic_square in magic_squares:
    cost = 0
    for i in range(9):
        cost += abs(arr[i]-magic_square[i])
    min_value = min(min_value, cost)
print(min_value)