# https://www.acmicpc.net/problem/15815
# 접근 방법
# 값을 차례로 스택에 넣어가며 연산자가 등장하면 해당 연산을 하고 스택에 값을 넣는다.
s = input()
stack = []
for x in s:
    if x in ['+', '-', '*', '/']:
        a = stack.pop()
        b = stack.pop()
        x = str(int(eval(b+x+a)))
    stack.append(x)
print(int(stack[0]))