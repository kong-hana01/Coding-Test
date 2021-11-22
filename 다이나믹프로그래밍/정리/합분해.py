# https://www.acmicpc.net/problem/2225
# 접근방법
# 위의 문제는 덧셈의 순서가 바뀐 경우는 다른 경우로 센다는 조건이 있다.
# 따라서 0 + 1과 1 + 0은 다른 경우의 수로 세는 것이다.
# 0부터 N까지의 정수에 대하며 K=2인 경우는 모두 N+1개가 있다.(0+N, 1+(N-1), ..., N+0)
# k=3일 때는 다음과 같은 식을 세울 수 있다.
# (0+(k=1일때 N개를 만들기 위한 경우의 수들), 1+(k=1일때 N-1개를 만들기 위한 경우이 수들), ..., N+0)
# 따라서 위의 식을 활용해 문제를 해결할 수 있다.

n, k = map(int, input().split())
d = [[0 for _ in range(n+1)] for _ in range(k)]
d[0][n] = 1

if k >= 2:
    for i in range(n+1):
        d[1][i] = i + 1 # 각 인덱스별로 n을 만들 수 있는 경우의 수 입력


    for i in range(2, k):
        for j in range(n+1):
            d[i][n-j] = sum(d[i-1][:n+1-j])

print(d[k-1][n] % 1000000000)
# print(d)