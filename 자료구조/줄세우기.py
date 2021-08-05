# https://www.acmicpc.net/problem/2631
# 접근방법
# 제일 긴 부분수열의 문제이다.
# 가장 긴 부분수열의 길이를 구한 뒤, 전체 인원수에서 뺀 값을 출력한다.
n = int(input())
array = [int(input()) for _ in range(n)]

d = [0] * (n)
result = 0
for i in range(n):
    value = 1
    for j in range(i):
        if array[i] > array[j]:
            value = max(value, d[j] + 1)
    d[i] = value
    result = max(result, value)
print(n-result)