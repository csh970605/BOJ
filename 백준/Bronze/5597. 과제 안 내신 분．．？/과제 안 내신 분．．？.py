# problem statement : https://www.acmicpc.net/problem/5597

students = [0]*30
for i in range(28):
    num = int(input()) - 1
    students[num] = 1

for i in range(len(students)):
    if students[i] == 0:
        print(i+1)