# 접근 방법
# 전형적인 이분매칭 문제이다.
# 직원번호를 인덱스로, 그 직원이 해야할 일을 값으로 가지는 직원 그래프, 일의 번호를 인덱스로, 그 일에 매칭이 된 직원의 번호를 값으로 가지는 리스트를 만든다.
# 이후 dfs를 통해 직원을 각 일에 매칭시켜준다.
# 단 각 사람 당 최대 두 개의 일을 맡을 수 있으므로 일의 개수를 저장할 리스트를 따로 만들어 일을 맡은 개수를 관리한다.
# 이미 한번 일을 맡은 직원의 경우 dfs를 통해 이분 매칭을 구현할 경우 맡은 일이 없어지지는 않기에 이를 고려하여 dfs를 구현한다.

def dfs(number):
    if visited[number]:
        return False
    visited[number] = True
    for t in employee[number]:
        if number != task[t] and (not task[t] or dfs(task[t])):
            task[t] = number
            return True
    return False

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
employee = [[] for _ in range(n+1)]
task = [0 for _ in range(m+1)]
count = [0 for _ in range(n+1)]
for i in range(1, n+1):
    temp = list(map(int, input().split()))
    employee[i] = temp[1:]

for number in range(1, n+1):
    visited = [False for _ in range(n+1)]
    dfs(number)
    visited = [False for _ in range(n+1)]
    dfs(number)

print(sum(1 for x in task if x > 0))
# print(task)