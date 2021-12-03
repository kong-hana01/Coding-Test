# https://www.acmicpc.net/problem/2810
n = int(input())
array = [x for x in input()]

count = 1
l = 0
for i in range(len(array)):
    if array[i] == 'S':
        count += 1
    else:  
        if l == 0:
            l += 1
        else:
            l = 0
            count += 1
if len(array) > count:
    print(count)
else:
    print(len(array))