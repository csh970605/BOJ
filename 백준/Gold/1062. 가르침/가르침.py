# problem statement : https://www.acmicpc.net/problem/1062
import sys
input = sys.stdin.readline

def backtrack(bitmask, index, learned):
    global max_count
    if learned == k:
        max_count = max(max_count, count_readable(bitmask))
        return
    for i in range(index, 26):
        if not (bitmask & (1 << i)):
            backtrack(bitmask | (1 << i), i + 1, learned + 1)
        
def count_readable(bitmask):
    count = 0
    for word in arr:
        readable = True
        for char in word:
            if not (bitmask & (1<<(ord(char)-ord('a')))):
                readable = False
                break
        if readable:
            count += 1
    return count
        
n, k = map(int, input().split())

arr = []
for _ in range(n):
    word = input().strip()
    arr.append(word[4:-4]) 
if k < 5:
    print(0)
    exit()
bitmask = 0
for char in ['a', 'n', 't', 'i', 'c']:
    bitmask |= (1 << (ord(char) - ord('a')))

max_count = 0
backtrack(bitmask, 0, 5)
print(max_count)