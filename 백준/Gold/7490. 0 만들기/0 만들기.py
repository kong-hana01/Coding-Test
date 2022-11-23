# https://www.acmicpc.net/problem/7490
# 접근 방법
# dfs를 활용한 브루트포스로 문제를 해결한다.
def dfs(idx, now, n):
    if idx == n:
        if eval("".join(now.split())) == 0:
            result.append(now)
        return
    dfs(idx+1, now+"+"+arr[idx], n)
    dfs(idx+1, now+"-"+arr[idx], n)
    dfs(idx+1, now+" "+arr[idx], n)    

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [str(i) for i in range(1, n+1)]
    result = []
    dfs(1, arr[0], n)
    result.sort()
    for x in result:
        print(x)
    print()