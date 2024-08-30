# problem statement : https://www.acmicpc.net/problem/1759
import sys
input = sys.stdin.readline

def backtracking(l, c, cs, arr, start, vowels):
    if len(cs) == l:
        vowelc = sum(1 for character in cs if character in vowels)
        if vowelc >= 1 and len(cs)-vowelc >= 2:
            print(''.join(map(str,cs)))
            return
    for i in range(start, c):
        if not visited[i]:
            visited[i] = 1
            cs.append(arr[i])
            backtracking(l, c, cs, arr, i+1, vowels)
            cs.pop()
            visited[i] = 0

l, c = map(int, input().split())

arr = list(map(str, input().split()))
arr.sort()
cs = []
visited = [0]*c
vowels = set('aeiou')
backtracking(l, c, cs, arr, 0, vowels)
