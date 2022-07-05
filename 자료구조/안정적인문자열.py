# https://www.acmicpc.net/problem/4889
# 접근 방법
# 스택을 통해 문제를 해결한다. 항상 짝수로 케이스를 고려하며 스택을 모두 탐색한 뒤에 짝을 지워준 뒤 {{, {}, }{, }}의 케이스가 있다고 가정하고 각 케이스별로 다음과 같이 동작하도록 한다.
# 1. {{: 우측 값을 }로 바꾸어 빼준다. +1
# 2. }{: 좌측과 우측이 값을 {}로 바꾸어 빼준다. +2
# 3. }}: 좌측 값을 {로 바꾸어 빼준다. +1
s = input()
tc = 1
while '-' not in s:
    stack = []
    count = 0
    for x in s:
        stack.append(x)
        while len(stack) >= 2:
            if stack[-2] == "{"  and stack[-1] == '}':
                stack.pop()
                stack.pop()
                continue
            break
    while stack:
        if stack[-2] == "{"  and stack[-1] == '{':
            stack.pop()
            stack.pop()
            count += 1
        elif stack[-2] == "}"  and stack[-1] == '{':
            stack.pop()
            stack.pop()
            count += 2
        else:
            stack.pop()
            stack.pop()
            count += 1
    print(f'{tc}. {count}')
    tc += 1
    s = input()