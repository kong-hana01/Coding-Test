# https://www.acmicpc.net/problem/9576
# 접근 방법
# DFS를 통해 이분매칭을 구현해 책을 나눠줄 수 있는 최대 학생 수를 출력한다.
import sys

def dfs(x):
    if visited[x]:
        return False
    visited[x] = True
    for i in s[x]:
        if not d[i] or dfs(d[i]):
            d[i] = x
            return True
    return False

input = sys.stdin.readline
for tc in range(int(input())):
    n, m = map(int, input().split())
    d = [0 for _ in range(n+1)] # 책
    s = [[] for _ in range(m+1)] # 학생이 선호하는 책 번호 저장
    for i in range(1, m+1):
        a, b = map(int, input().split())
        for j in range(a, b+1):
            s[i].append(j) # 각 학생이 선호하는 책의 번호 저장
    for i in range(1, m+1):
        visited = [False for _ in range(m+1)] # 책(d)에 대한 방문 처리
        dfs(i)
    print(sum([1 for x in d if x > 0]))