# problem statement : https://www.acmicpc.net/problem/2448
import sys
input = sys.stdin.readline

def dfs(n):
    if n == 3:
        return ['  *  ', ' * * ', '*****']
    
    stars = dfs(n//2)
    result = []
    
    for star in stars:
        result.append(' '*(n//2)+star+' '*(n//2))
    
    for star in stars:
        result.append(star+' '+star)
    
    return result

n = int(input())
result = dfs(n)
print('\n'.join(result))