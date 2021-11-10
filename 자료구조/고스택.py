# https://www.acmicpc.net/problem/3425
# 접근 방법
# 주어진 명령어를 함수로 구현해 이를 동작시킨다.
def programming(num):
    stack = [num]
    for x in program:
        if x == "POP":
            if len(stack) == 0:
                return False
            stack.pop()
        elif x == "INV":
            if len(stack) == 0:
                return False
            stack[-1] = -stack[-1]
        elif x == 'DUP':
            if len(stack) == 0:
                return False
            stack.append(stack[-1])
        elif x == 'SWP':
            if len(stack) < 2:
                return False
            stack[-1], stack[-2] = stack[-2], stack[-1]
        elif x == 'ADD':
            if len(stack) < 2:
                return False
            x1 = stack.pop()
            x2 = stack.pop()
            if abs(x2 + x1) > 1e9:
                return False
            stack.append(x1 + x2)
        elif x == 'SUB':
            if len(stack) < 2:
                return False
            x1 = stack.pop()
            x2 = stack.pop()
            if abs(x2 - x1) > 1e9:
                return False
            stack.append(x2 - x1)
        elif x == 'MUL':
            if len(stack) < 2:
                return False
            x1 = stack.pop()
            x2 = stack.pop()
            if abs(x1 * x2) > 1e9:
                return False
            stack.append(x2 * x1)           
        elif x == 'DIV':
            if len(stack) < 2 or (len(stack) >= 2 and stack[-1] == 0):
                return False
            x1 = stack.pop()
            x2 = stack.pop()
            signx1 = 1 if x1 >= 0 else -1 
            signx2 = 1 if x2 >= 0 else -1
            stack.append((abs(x2) // abs(x1)) * signx1 * signx2)
        elif x == 'MOD':
            if len(stack) < 2 or (len(stack) >= 2 and stack[-1] == 0):
                return False
            x1 = stack.pop()
            x2 = stack.pop()
            signx1 = 1 if x1 >= 0 else -1 
            signx2 = 1 if x2 >= 0 else -1
            stack.append((x2%x1) * signx2)
        else:
            stack.append(int(x.split()[1]))

    return stack


program = []
while True:
    commend = input()
    if commend == "END":
        n = int(input())
        for _ in range(n):
            num = int(input())
            stack = programming(num)
            if stack:
                if len(stack) == 1 and abs(stack[0]) <= 1e9:
                    print(stack[0])
                else:
                    print("ERROR")
            else:
                print("ERROR")

        program.clear()
        print('\n')
        continue
        
    elif commend == "QUIT":
        break

    elif commend == '':
        continue

    program.append(commend)
