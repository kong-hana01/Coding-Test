# https://www.acmicpc.net/problem/1934
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(a * b // gcd(a, b))