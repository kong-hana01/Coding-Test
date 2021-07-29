# https://www.acmicpc.net/problem/1074
# 접근 방법
# 2의 n제곱 x 2의 n제곱을 4등분하면 2의 n-1제곱 x 2의 n-1제곱의 형태가 된다.
# 주어진 r과 c를 위와 같이 범위를 줄여가며 찾는다.
# r기준으로 2의 k제곱보다 크다면 2의 k제곱의 곱하기 2만큼 결과값에 더해준다.
# c기준으로 2의 k제곱보다 크다면 2의 k제곱만큼 결과값에 더해준다.

n, r, c = map(int, input().split())

result = 0
while n > 0:
    n -= 1
    if 2 ** n <= r:
        result += ((2 ** n) ** 2) * 2
        r -= 2 ** n
    if 2 ** n <= c:
        result += (2 ** n) ** 2
        c -= 2 ** n
print(result)