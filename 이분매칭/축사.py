# 접근 방법
# 전형적인 이분매칭 문제이다.
# 소의 번호를 인덱스로하고 가고싶은 축사의 번호를 값으로 갖는 리스트(cow)를 만들고 축사의 번호를 인덱스로하고 그 축사에 배정받은 소의 번호를 값으로 갖는 리스트(cattle_shed)를 만든다.
# 이후 dfs를 통해 이분매칭을 구현한다.

import sys

def dfs(cow_number):
    if visited[cow_number]:
        return False
    visited[cow_number] = True
    
    for i in cow[cow_number]:
        if not cattle_shed[i] or dfs(cattle_shed[i]):
            cattle_shed[i] = cow_number
            return True
            
    return False
            
input = sys.stdin.readline
n, m = map(int, input().split())
cow = [[] for _ in range(n+1)]
cattle_shed = [0 for _ in range(m+1)]
for i in range(1, n+1):
    array = list(map(int, input().split()))
    for j in array[1:]:
        cow[i].append(j)
        
for i in range(1, n+1):
    visited = [False for _ in range(n+1)]
    dfs(i)
    
print(sum([1 for i in cattle_shed if i > 0]))