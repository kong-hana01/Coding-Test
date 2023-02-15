# https://www.acmicpc.net/problem/9996
# 접근 방법
# 요구사항대로 문제를 해결한다.
n = int(input())
pattern = input().split("*")
for _ in range(n):
    x = input()
    start_size = len(pattern[0])
    end_size = len(pattern[1])
    if len(x) >= start_size + end_size and x[:start_size] == pattern[0] and x[-end_size:] == pattern[1]:
        print("DA")
    else:
        print("NE")