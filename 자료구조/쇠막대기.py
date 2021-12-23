# https://www.acmicpc.net/problem/10799
# 접근 방법
# 0. 스택으로 괄호 표현을 하나씩 저장한다. 
# 1. )가 나온다면 스택의 마지막 값을 빼내어주고 현재 저장되어있는 값을 더해준다. (해당 값이 현재 막대기의 개수이기 때문이다.)
# 2. 모든 괄호를 탐색한 뒤, 누적해서 더한 값을 출력한다.
bracket = input()
stack = []
result = 0
for i in range(len(bracket)-1):
    if bracket[i] == '(' and bracket[i+1] == ')':
        print(len(stack))
        result += len(stack) + 1 if stack else 0
    elif bracket[i] == "(":
        stack.append(bracket[i])
    elif bracket[i] == ")" and bracket[i+1] == ")":
        stack.pop()

print(result)