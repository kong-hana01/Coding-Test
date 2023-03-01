# https://www.acmicpc.net/problem/9093
t = int(input())
for _ in range(t):
    s = input().split()
    print(" ".join(list(map(lambda x: x[::-1], s))))