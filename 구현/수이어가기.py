# https://www.acmicpc.net/problem/2635
# 접근 방법
# 주어진 수에서 절반 이상에 대한 값들을 탐색하며 매번 주어진 규칙에 따라 리스트의 값을 추가하여 가장 길이가 긴 리스트의 값을 출력한다.
n = int(input())
result = [n]
for i in range(n//2, n):
    temp = [n, i]
    while temp[-2] - temp[-1] >= 0:
        temp.append(temp[-2] - temp[-1])
    if len(temp) > len(result):
        result = temp

print(len(result))
for x in result:
    print(x,end=' ')