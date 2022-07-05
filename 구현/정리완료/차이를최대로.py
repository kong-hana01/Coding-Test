# https://www.acmicpc.net/problem/10819
# 접근 방법
# 브루트포스로 모든 경우의 수를 모두 구한다.
n = int(input())
arr = list(map(int, input().split()))
visited = [False for _ in range(n)]
def findMaxValue(temp):
    value = 0
    for i in range(n-1):
        value += abs(temp[i] - temp[i+1])
    return value

def createArr(temp):
    if len(temp) == n:
        global maxValue
        maxValue = max(findMaxValue(temp), maxValue)
        return 
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            createArr(temp+[arr[i]])
            visited[i] = False

maxValue = 0
createArr([])
print(maxValue)