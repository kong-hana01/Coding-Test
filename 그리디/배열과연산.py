# https://www.acmicpc.net/problem/14222
# 접근방법
# 현재 배열을 모두 탐색한 뒤, dp 테이블에 1을 저장한다.
# 이후 0이 있는 테이블을 하나씩 탐색하며 k만큼 뺀 뒤, 해당 인덱스에 1이 있다면 1을 저장한다.
# 위의 과정을 반복한 뒤, 0을 제외한 모든 dp 테이블에 1이 있다면 1, 아니라면 0을 출력한다.
n, k = map(int, input().split())
dp = [0 for _ in range(n+1)]
arr = list(map(int, input().split()))
for x in arr:
    if x <= n:
        dp[x] += 1

for x in range(1, n+1):
    if dp[x] == 0:
        if x - k <= 0:
            break
        if dp[x - k]:
            dp[x] = 1
            dp[x - k] -= 1

print(dp)
