# https://www.acmicpc.net/problem/12919
# 접근 방법
# t를 s로 만든다.
def dfs(now):
    if len(s) == len(now):
        if now == s:
            return True
        return False
    visited[now] = True
    if now[-1] == "A" and now[:-1] not in visited:
        if dfs(now[:-1]):
            return True
    if now[0] == "B" and now[::-1][:-1] not in visited:
        if dfs(now[::-1][:-1]):
            return True
    return False

s = input()
t = input()
visited = {}
if dfs(t):
    print(1)
else:
    print(0)