# problem statement : https://www.acmicpc.net/problem/25305

n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort(reverse=True)
print(arr[k-1])