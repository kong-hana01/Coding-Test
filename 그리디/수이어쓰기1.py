# https://www.acmicpc.net/problem/1748
# 접근 방법
# 자리수가 늘어갈때마다 이전 자리수에서 더했던 숫자 + 10을 하여 구한다.
n = input()
result = ((int(n) - 10 ** (len(n) - 1)) + 1) * len(n)
for i in range(1, len(n)):
    result += 9 * i * 10 ** (i-1)
print(result)