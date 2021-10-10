# https://www.acmicpc.net/problem/16916
# 접근 방법
# 스택을 통해 부분문자열을 구한다.
import sys
input = sys.stdin.readline

s = input()
p = input()
stack = []
check = 0
result = 0
for x in s:
    stack.append(x)
    check = max(0, check - 1)
    if not check and len(stack) >= len(p):
        for i in range(len(p)):
            print(stack[len(stack) - len(p) + i])
            if stack[len(stack) - len(p) + i] != p[i]:
                check =len(stack) - len(p) + i + 1
        if not check:
            result = 1
            break
print(result)