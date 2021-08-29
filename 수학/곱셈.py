# https://www.acmicpc.net/problem/1629
# 접근 방법 2 (나중에 다시 한번 더 풀어보기)
# n이 짝수일 때 a**(b//2) x a**(b//2)로 분할할 수 있다.
# n이 홀수일 때 a x a**(b//2) x a**(b//2)의 형태로 분할할 수 있다.
# 위와 같은 제곱의 특성을 활용해 나머지를 구한다.
a, b, c = map(int, input().split())

def square(a, b, c):
    if b == 2:
        return a ** 2 % c
    elif b == 1:
        return a % c
    elif b % 2 == 0:
        return square(a, b//2, c) ** 2 % c
    else:
        return square(a, 1, c) * (square(a, (b-1)//2, c) ** 2) % c

print(square(a, b, c))





# 접근 방법 1 -> 메모리 초과 2의 31승을 계산할 수 없음
# b = 1일 때의 문제의 식은 다음과 같이 나타낼 수 있다.
# f(x) = a // c + a % c
# b = 2일 때의 문제의 식은 다음과 같이 나타낼 수 있다.
# f(x) = a ** 2 // c + a ** 2 % c = a(a // c + a % c)
# b = n일 때 문제의 식은 다음과 같이 나타낼 수 있다.
# f(x) = a ** n // c + a ** n % c = a**(n-1)(a // c + a % c)
# 우리가 구하고자 하는 것은 나머지이므로 a를 c로 나눈 나머지에 a를 곱하고 다시 c로 나누는 과정을 n번만큼 반복하면 문제를 해결할 수 있다.

# import sys
# sys.setrecursionlimit(2**31-1)
# a, b, c = map(int, input().split())
# def multiply(a, b, c):
#     if b == 1:
#         return a % c
#     print(a, b, c)
#     return a * (multiply(a, b-1, c)) % c

# print(multiply(a, b, c))

