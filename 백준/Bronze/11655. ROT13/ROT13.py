# problem statement : https://www.acmicpc.net/problem/11655
import sys
input = sys.stdin.readline

string = input()
arr = []

for char in string:
    if 'A' <= char <= 'Z':
        char = ord(char) + 13
        if char > ord('Z'):
            char = char - ord('Z') + ord('A') - 1
        char = chr(char)
    elif 'a' <= char <= 'z':
        char = ord(char) + 13
        if char > ord('z'):
            char = char - ord('z') + ord('a') - 1
        char = chr(char)
    arr.append(char)

print(''.join(arr))
