# problem statement : https://www.acmicpc.net/problem/2529
import sys
input = sys.stdin.readline

def backtrack(index, num):
    if index == n+1:
        result.append(num)
        return
    
    for i in range(10):
        if not visited[i] and (index == 0 or (arr[index-1] == '<' and num[-1] < str(i)) or (arr[index-1] == '>' and num[-1] > str(i))):
            visited[i] = True
            backtrack(index+1, num+str(i))
            visited[i] = False

result = []
n = int(input())
arr = list(map(str, input().split()))
visited = [0]*10

backtrack(0, '')
print(max(result))
print(min(result))