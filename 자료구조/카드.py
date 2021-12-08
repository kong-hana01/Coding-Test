# https://www.acmicpc.net/problem/11652
# 접근 방법
# 딕셔너리 형태로 해당 값을 키로, 그 수의 count를 밸류로 저장하여, 가장 많이 나온 값을 출력한다.
import sys
input = sys.stdin.readline
n = int(input())
cardDict = {}
cardSet = set()
for _ in range(n):
    x = int(input())
    if x not in cardSet:
        cardDict[x] = 0
        cardSet.add(x)
    cardDict[x] += 1


count = 0
result = 2**62
for key, value in cardDict.items():
    if count < value:
        count = value
        result = key
    elif count == value:
        result = min(result, key)
            
print(result)
