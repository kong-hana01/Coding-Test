# https://www.acmicpc.net/problem/1057
n, num1, num2 = map(int, input().split())
arr = [i+1 for i in range(n)]

round = 0
is_fight = False
while arr and not is_fight:
    temp = []
    for i in range(0, len(arr)-1, 2):
        if arr[i] in [num1, num2] and arr[i+1] in [num1, num2]:
            is_fight = True
            break
        if arr[i] in [num1, num2]:
            temp.append(arr[i])
        elif arr[i+1] in [num1, num2]:
            temp.append(arr[i+1])
        else:
            temp.append(arr[i])
    if len(arr) % 2 == 1:
        temp.append(arr[-1])
    round += 1
    arr = temp
    
print(round)