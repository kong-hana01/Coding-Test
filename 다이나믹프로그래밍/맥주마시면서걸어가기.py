# https://www.acmicpc.net/problem/11060
# 접근 방법
# 다이나믹 프로그래밍을 통해 각 위치에서 이동할 수 있는 곳에서 가장 작은 점프 횟수를 저장해나간다.
n = int(input())
arr = list(map(int, input().split()))
dp = [n for _ in range(n)]
dp[0] = 0
for i in range(n):
    num = arr[i]
    for jump in range(i+1, min(i+num+1, n)):
        dp[jump] = min(dp[jump], dp[i]+1)
print(dp[-1] if dp[-1] < n else -1)