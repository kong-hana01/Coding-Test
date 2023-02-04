# https://www.acmicpc.net/problem/20365
# 접근 방법
# 연속된 수의 개수를 체크한다.
n = int(input())
s = input()
last = s[0]
color = {"B": 0, "R": 0}
color[last] = 1
for i in range(1, n):
    if s[i] == last:
        continue
    last = s[i]
    color[last] += 1
print(min(color["B"], color["R"]) + 1)