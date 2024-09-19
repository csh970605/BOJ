# problem statement : https://www.acmicpc.net/problem/2263
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000000)

def dfs(in_s, in_e, post_s, post_e):
    if in_s > in_e or post_s > post_e:
        return
    root = postorder[post_e]
    print(root, end=' ')
    root_idx = inorder_idx[root]
    left = root_idx - in_s
    dfs(in_s, root_idx-1, post_s, post_s+left-1)
    dfs(root_idx+1, in_e, post_s+left, post_e-1)


n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
inorder_idx = [0]*(n+1)
for i in range(n):
    inorder_idx[inorder[i]] = i

dfs(0, n-1, 0, n-1)