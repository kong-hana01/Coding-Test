import sys
n = int(sys.stdin.readline())
orders = [list(sys.stdin.readline().split()) for _ in range(n)]
# n = 14
# orders = [['push', '1'], ['push', '2'], ['top'], ['size'], ['empty'], ['pop'], ['pop'], ['pop'], ['size'], ['empty'], ['pop'], ['push', '3'], ['empty'], ['top']]

stack = []
for order in orders:
    if order[0] == 'push':
        stack.append(int(order[1]))

    elif order[0] == 'pop':
        if stack:
            x = stack.pop()
            print(x)
        else:
            print(-1)

    elif order[0] == 'size':
        print(len(stack))
    
    elif order[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif order[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)