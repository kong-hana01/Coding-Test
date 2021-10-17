# https://www.acmicpc.net/problem/13913
# 접근 방법
# bfs를 통해 이전 지역에서 다음 지역으로 이동할 때, 다음 지역에 값이 있는지 없는지를 확인하며 탐색한다.
# 단 리스트의 값은 이전 위치로 갱신한다.
# dp[k]의 값이 갱신된다면 탐색을 멈추고 dfs를 통해 이전 위치의 값을 스택에 저장하고, dfs 탐색이 끝나면 스택의 길이 - 1을 출력하고 스택의 값을 pop하며 하나씩 출력한다.
def dfs(idx):
    stack.append(idx)
    if dp[idx] == idx:
        return 
    return dfs(dp[idx])

from collections import deque
import sys
sys.setrecursionlimit(10**6)
n, k = map(int, input().split())
dp = [-1 for _ in range(200000)]
dp[n] = n
queue = deque([])
queue.append(n)
while dp[k] == -1:
    x = queue.popleft()

    if x + 1 < len(dp) and dp[x+1] == -1:
        dp[x+1] = x
        queue.append(x+1)
    
    if x - 1 >= 0 and dp[x-1] == -1:
        dp[x-1] = x
        queue.append(x-1)
    
    if x * 2 < len(dp) and dp[x*2] == -1:
        dp[x*2] = x
        queue.append(x*2)

stack = []
dfs(k)
print(len(stack) - 1)
while stack:
    x = stack.pop()
    print(x, end=' ')