# https://www.acmicpc.net/problem/9461
# 접근방법
# 나선에서 가장 큰 변을 변으로 가지는 정삼각형을 계속 만들다보면 정삼각형 4개를 이어붙일 때부터 오각형이 된다. 이를 계속 반복하더라도 오각형의 형태는 유지한다.
# 정삼각형 5개를 이어붙인 뒤에는 가장 큰 변과 아직 하나의 변이라도 삼각형이 이어붙이지 않은 변이 있는 삼각형 중 가장 작은 변의 합으로 k가 결정된다.
# 위의 특징을 활용해 dp테이블을 만든다.
dp = [0] * 101
dp[1], dp[2], dp[3], dp[4], dp[5] = 1, 1, 1, 2, 2

i = 6
while i <= 100:
    dp[i] = dp[i-1] + dp[i - 5]
    i += 1

for tc in range(int(input())):
    n = int(input())
    print(dp[n])
