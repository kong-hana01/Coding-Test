# https://www.acmicpc.net/problem/1817
# 접근 방법
# 요구사항대로 구현한다.
n, m = map(int, input().split())
cnt = 0

if n:
    arr = list(map(int, input().split()))
    now = m
    for x in arr:
        if now + x > m:
            cnt += 1
            now = 0
        now += x
print(cnt)