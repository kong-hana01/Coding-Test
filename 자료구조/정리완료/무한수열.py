# https://www.acmicpc.net/problem/1351
# 접근방법
# 딕셔너리를 활용해 트리구조를 구현하여 다이나믹프로그래밍을 동작시켜 An을 구한다.
def dfs(x):
    if x in idx:
        return tree[x]
    value = dfs(x//p) + dfs(x//q)
    tree[x] = value
    idx.add(x)
    return value

n, p, q = map(int, input().split())
tree = {}
tree[0] = 1
idx = set()
idx.add(0)
print(dfs(n))