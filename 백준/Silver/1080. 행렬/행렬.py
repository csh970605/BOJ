# problem statement : https://www.acmicpc.net/problem/1080
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
start_arr = []
end_arr =[]
for _ in range(n):
    start_arr.append(list(map(int, input().strip())))
for _ in range(n):
    end_arr.append(list(map(int, input().strip())))
count = 0
for i in range(n-2):
    for j in range(m-2):
        if start_arr[i][j] != end_arr[i][j]:
            for k in range(3):
                for l in range(3):
                    start_arr[i+k][j+l] = 1 - start_arr[i+k][j+l]
            count +=1
if start_arr == end_arr:
    print(count)
else:
    print(-1)