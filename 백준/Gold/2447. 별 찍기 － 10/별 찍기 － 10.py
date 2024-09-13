# problem statement : https://www.acmicpc.net/problem/2447
import sys
input = sys.stdin.readline

def dfs(n):
    if n == 1:
        return ['*']
    
    stars = dfs(n // 3)
    result = []

    for i in range(3):
        for star in stars:
            if i == 1:
                result.append(star+' '*(n//3)+star)
            else:
                result.append(star*3)
    return result

n = int(input())
result = dfs(n)
print('\n'.join(result))