# https://www.acmicpc.net/problem/1662
# 접근 방법
# 문자열을 하나씩 탐색하며 (가 등장하면 그 앞의 숫자를 다른 스택에 저장한다.
# 이후 숫자를 하나씩 세어 가며 )가 등장할 경우 해당 숫자를 스택의 마지막에 저장되어있는 숫자만큼 곱한 뒤, 이를 이전에 세었던 숫자에 더해준다.
# 위의 과정을 반복하며 최종 문자열의 길이를 출력한다.

s = input()
stack = []
stack.append([0, 1])
for i in range(len(s)):
    if s[i] != '(' and s[i] != ')':
        stack[-1][0] += 1
    else:
        if s[i] == '(':
            stack[-1][0] -= 1
            stack.append([0, int(s[i-1])])

        if s[i] == ')':
            count, mul = stack.pop()
            stack[-1][0] += count * mul
            
print(stack[0][0])