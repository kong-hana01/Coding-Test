# https://www.acmicpc.net/problem/9613
# 접근 방법
# 가능한 모든 경우의 수에 대해 GCD 합을 구해 출력한다.
def gcd(a, b):
    if a % b:
        return gcd(b, a%b)
    return b

t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    result = 0
    for i in range(1, arr[0]+1):
        for j in range(i+1, arr[0]+1):
            result += gcd(max(arr[i], arr[j]), min(arr[i], arr[j]))
    print(result)