# https://www.acmicpc.net/problem/11406
# 접근 방법
# 이분매칭을 통해 문제를 해결한다. 
def dfs(number):
    if visited[number]:
        return False
    visited[number] = True
    for bookstore_number in customers[number]:
        if bought[bookstore_number][number] < capacity[bookstore_number][number]:
            for i in range(len(bookstores[bookstore_number])):
                if bookstores[bookstore_number][i] == -1:
                    bookstores[bookstore_number][i] = number
                    bought[bookstore_number][number] += 1
                    return True
            for i in range(len(bookstores[bookstore_number])):
                if dfs(bookstores[bookstore_number][i]):
                    bought[bookstore_number][bookstores[bookstore_number][i]] -= 1
                    bookstores[bookstore_number][i] = number
                    bought[bookstore_number][number] += 1
                    return True
    return False                

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
want_to_buy = list(map(int, input().split()))
bookstores = [[-1 for _ in range(x)] for x in list(map(int, input().split()))]
capacity = [list(map(int, input().split())) for _ in range(m)]
bought = [[0 for _ in range(n)] for _ in range(m)]
customers  = [[] for _ in range(n)]
for i in range(m):
    for j in range(n):
        for k in range(capacity[i][j]):
            customers[j].append(i)
result = 0
for i in range(n):
    for cnt in range(want_to_buy[i]):
        visited = [False for _ in range(n)]
        if dfs(i):
            result += 1
print(result)
    