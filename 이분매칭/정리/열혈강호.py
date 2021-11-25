# 접근 방법
# 전형적인 이분 매칭 문제이다.
# 직원의 번호를 인덱스로 하고, 할 수 있는 일의 번호를 값으로 가지는 리스트(employee)와 일의 번호를 인덱스로 하고, 그 일을 하는 직원의 번호를 값으로 가지는 리스트(work)를 초기화한다.
# 이후 dfs를 통해 이분매칭을 구현한다.

def dfs(employee_number):
    if visited[employee_number]:
        return False
        
    visited[employee_number] = True
    for work_number in employee[employee_number]:
        if not work[work_number] or dfs(work[work_number]):
            work[work_number] = employee_number
            return True
    
    return False

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
employee = [[]]
for _ in range(n):
    temp = list(map(int, input().split()))
    employee.append(temp[1:])
work = [0 for _ in range(m+1)]
for i in range(1, n+1):
    visited = [False for _ in range(n+1)]
    dfs(i)
print(sum([1 for x in work if x > 0]))