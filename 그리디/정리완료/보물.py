# https://www.acmicpc.net/problem/1026
# 접근 방법
# a는 오름차순, b는 내림차순으로 정렬해 각 값을 곱한 것을 출력한다.
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse = True)
result = 0
for i in range(n):
    result += a[i] * b[i]
print(result)