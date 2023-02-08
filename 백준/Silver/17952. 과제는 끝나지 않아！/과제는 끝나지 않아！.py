# https://www.acmicpc.net/problem/17952
# 접근 방법
# 스택을 사용해 문제를 해결한다.
n = int(input())
result = 0
stack = []
for _ in range(n):
    homework = list(map(int, input().split()))
    if homework[0] == 0:
        if stack:
            h = stack.pop()
            h[1] -= 1
            if h[1] == 0:
                result += h[0]
            else:
                stack.append(h)
        continue
    a, t = homework[1:]
    if t == 1:
        result += a
    else:
        stack.append([a, t-1])
print(result)