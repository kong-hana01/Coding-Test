# https://www.acmicpc.net/problem/11899
# 접근 방법
# 스택에 괄호를 넣고 모두 넣은 뒤 남은 문자가 몇 개 있는지 출력한다.
s = input()
stack = []
for x in s:
    stack.append(x)
    while len(stack) >= 2 and stack[-2] == '(' and stack[-1] == ')':
        stack.pop()
        stack.pop()
print(len(stack))