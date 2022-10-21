# https://www.acmicpc.net/problem/11066
# 접근 방법
# dp[i][j] = min(dp[i][k] + dp[k+1][j] + A[i][j]) 단, i<=k<=j-1의 점화식을 가지고 문제를 해결한다.
# dp는 여태 i~j까지 누적해서 더했을 때의 최종 비용을 의미하고, A는 i~j까지 배열을 더했을 때의 파일 크기의 합을 의미한다.
t = int(input())
for _ in range(t):
    k = int(input())
    arr = list(map(int, input().split()))
    INF = int(1e9)
    A = [[0 for _ in range(k)] for _ in range(k)]
    dp = [[INF for _ in range(k)] for _ in range(k)]
    for i in range(k):
        A[i][i] = arr[i]
        dp[i][i] = 0

    for dialog in range(1, k):
        for i in range(k-dialog):
            j = i + dialog
            A[i][j] = A[i][j-1] + arr[j]

    for dialog in range(1, k):
        for i in range(k-dialog):
            j = i + dialog
            for v in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][v] + dp[v+1][j])
            dp[i][j] += A[i][j]
    print(dp[0][k-1])