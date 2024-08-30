# problem statement : https://www.acmicpc.net/problem/1620

n, m = list(map(int, input().split()))
alpha_dict = {}
str_dict = {}
for i in range(1, n+1):
    s = input().strip()
    alpha_dict[s] = i
    str_dict[i] = s
nums = []
for _ in range(m):
    nums.append(input().strip())

for num in nums:
    try:
        num = int(num)
        print(str_dict[num])
    
    except BaseException:
        num = str(num)
        print(alpha_dict[num])