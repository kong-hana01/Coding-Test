# https://www.acmicpc.net/problem/11066
# 접근 방법
# 다이나믹프로그래밍을 사용해 최소 비용을 구한다.
def dfs(row, col):
    if dp[row][col]:
        return dp[row][col]
    left_r, left_c = row+1, col # row는 하나씩 +1
    right_r, right_c = k-1, k-(row+1)+left_c # row는 하나씩 -1, col도 하나씩 -1
    for _ in range(k-(row+1)):
        left = dfs(left_r, left_c)
        right = dfs(right_r, right_c)
        if result[row][col] > result[left_r][left_c] + result[right_r][right_c] + left+right:
            dp[row][col] = left+right
            result[row][col] = result[left_r][left_c] + result[right_r][right_c] + left+right
        left_r += 1
        right_r -= 1
        right_c -= 1
        
    return dp[row][col]

import sys
input = sys.stdin.readline
for tc in range(int(input())):
    k = int(input())
    dp = [[0 for _ in range(i+1)] for i in range(k-1)]
    dp.append(list(map(int, input().split())))
    result = [[int(1e9) for _ in range(i+1)] for i in range(k-1)]
    result.append([0 for _ in range(k)])
    dfs(0, 0)
    print(result[0][0])