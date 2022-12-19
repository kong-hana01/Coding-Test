# https://www.acmicpc.net/problem/1935
# 접근 방법
# 스택을 사용해 문제를 해결한다.
n = int(input())
arr = input()
stack = []
alpha = {}
for i in range(ord("A"), ord("A") + n):
    v = input()
    alpha[chr(i)] = v 
for x in arr:
    if x in ["*", "+", "-", "/"]:
        a = stack.pop()
        b = stack.pop()
        result = str(eval(b + x + a))
        stack.append(result)
        continue
    stack.append(alpha[x])
print("{:.2f}".format(float(stack[0])))