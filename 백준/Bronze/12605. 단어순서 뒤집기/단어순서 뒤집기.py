# https://www.acmicpc.net/problem/12605
n = int(input())
for i in range(1, n+1):
    arr = input().split()
    result = " ".join(arr[::-1])
    print(f"Case #{i}: {result}")