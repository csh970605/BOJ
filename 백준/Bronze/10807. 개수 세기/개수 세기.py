input1 = int(input())
input2 = input()
input3 = int(input())
result = 0
nums = map(int, input2.split())
for num in nums:
    if num == input3:
        result +=1

print(result)