# problem statement : https://www.acmicpc.net/problem/11478

s = input().strip()
arr = set()
for i in range(len(s)):
    for j in range(0, len(s)):
        arr.add(s[i:j+1])
print(len(arr)-1)