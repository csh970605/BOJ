# problem statement : https://www.acmicpc.net/problem/10820
import sys
input = sys.stdin.readline

while True:
    string = input()
    if not string:
        break
    arr = [0, 0, 0, 0]
    for char in string:
        if 'A' <= char <= 'Z':
            arr[1] += 1
        elif 'a' <= char <= 'z':
            arr[0] += 1
        elif char == ' ':
            arr[3] += 1
        elif '0' <= char <= '9':
            arr[2] += 1

    print(' '.join(map(str, arr)))