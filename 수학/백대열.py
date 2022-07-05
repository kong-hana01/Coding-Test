# https://www.acmicpc.net/problem/14490
# 접근 방법
# GCD를 사용해 문제를 해결한다.
def gcd(a, b):
    if a % b:
        return gcd(b, a%b)
    return b

n, m = map(int, input().split(':'))
print(n//gcd(n, m), ":", m//gcd(n, m), sep='')