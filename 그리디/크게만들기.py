# https://www.acmicpc.net/problem/2812
# 접근방법
# 가장 자리수가 높은 숫자는 가장 숫자가 커야하기 때문에 앞에 숫자부터 하나씩 탐색하며 앞에 숫자가 뒤에 나오는 숫자보다 작을 경우 이를 빼준다.
# 한번 빼줄때마다 해당 위치에서부터 차례대로 다시 탐색을 진행한다.
# 만약 전부 탐색을 진행했음에도 더이상 뺄 숫자가 없다면 제일 뒤에 있는 숫자를 빼야하는 남은 숫자만큼 뺀다.
n, k = map(int, input().split())
number = [x for x in input()]

array = [int(number[0])]

i = 1
while i < len(number):
    while len(array) > 0 and int(number[i]) > array[-1]:
        if k == 0:
            break
        array.pop()
        k -= 1 
    array.append(int(number[i]))
    # print('number[i]: ', number[i])
    # print('array: ', array)
    i += 1

while k > 0:
    array.pop()
    k -= 1

for x in array:
    print(x, end = '')