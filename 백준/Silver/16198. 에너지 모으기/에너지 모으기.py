# problem statement : https://www.acmicpc.net/problem/16198
import sys
input = sys.stdin.readline

def backtrack(energy_sum):
    global energy
    if sum(removed) == n-2:
        energy = max(energy, energy_sum)
        return
    for i in range(1, n-1):
        if not removed[i]:
            left = i - 1
            while removed[left] and left >= 0:
                left -= 1
            right = i + 1
            while removed[right] and right <= n-1:
                right += 1
            gained = balls[left]*balls[right]
            removed[i] = 1
            backtrack(gained+energy_sum)
            removed[i] = 0
n = int(input())
balls = list(map(int, input().split()))
removed = [0]*n
energy = 0
backtrack(0)
print(energy)