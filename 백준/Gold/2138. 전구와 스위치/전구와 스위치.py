# problem statement : https://www.acmicpc.net/problem/2138
import sys
input = sys.stdin.readline

def count_switches(start, end, n):
    arr = start[:]
    count = 0
    for i in range(1, n):
        if arr[i-1] != end[i-1]:
            toggle(arr, i)
            count += 1
    if arr == end:
        return count
    else:
        return float('inf')
    
def toggle(arr, idx):
    for i in range(idx-1, idx+2):
        if 0 <= i < len(arr):
            arr[i] = 1 - arr[i]

n = int(input())
start_arr = list(map(int, input().strip()))
end_arr = list(map(int, input().strip()))
               
result_1 = count_switches(start_arr, end_arr, n)

start_arr2 = start_arr[:]
toggle(start_arr2, 0)
result_2 = count_switches(start_arr2, end_arr, n) + 1

result = min(result_1, result_2)
if result == float('inf'):
    print(-1)
else:
    print(result)