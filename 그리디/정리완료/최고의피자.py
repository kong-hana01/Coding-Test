# https://www.acmicpc.net/problem/5545
# 접근 방법
# 피자 토핑의 열량을 내림차순 정렬하여 이를 계산한다.
n = int(input())
a, b = map(int, input().split())
c = int(input())
topping = [int(input()) for _ in range(n)]
topping.sort(reverse=True)
result = c // a
d = c
price = a
for k in range(n):
    price += b
    d += topping[k]
    result = max(result, d // price)
print(result)