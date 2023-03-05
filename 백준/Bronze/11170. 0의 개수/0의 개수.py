# https://www.acmicpc.net/problem/11170
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    result = 0
    for i in range(n, m+1):
        result += str(i).count("0")
    print(result)