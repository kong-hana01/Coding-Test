# https://www.acmicpc.net/problem/14728
# 접근 방법
# 각 단원별로 총 시간에 대해 탐색을 진행한 뒤, 다음과 같은 점화식을 세워 문제를 해결한다.
# d[i] = max(d[i-k] + s, d[i]), k는 각 단원별 공부 시간, s는 그 단원 문제의 배점
# 이때 앞에서부터 값을 갱신할 경우에는 이전 값을 누적해서 더하기 때문에 t시간부터 k시간까지 값을 줄여가서 카운트한다.
n, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(t+1)]
for k, s in arr:
    for i in range(t, k-1, -1):
        dp[i] = max(dp[i], dp[i-k] + s)
print(dp[t])