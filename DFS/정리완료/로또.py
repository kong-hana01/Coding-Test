# https://www.acmicpc.net/problem/6603
# 접근 방법
# DFS를 통해 최대 6개의 숫자를 뽑아 이를 출력한다.
def dfs(caseOfLotto, idx):
    if len(caseOfLotto) == 6:
        for l in caseOfLotto:
            print(l, end = ' ')
        print()
        return
        
    for i in range(idx, len(lotto)):
        dfs(caseOfLotto + [lotto[i]], i+1)


while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    lotto = arr[1:]
    dfs([], 0)
    print()