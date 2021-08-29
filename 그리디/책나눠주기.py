# 추후 재도전 -> 이분매칭 공부 후 도전
# 접근방법
# 1. 주어진 m을 시작점(a)을 기준으로 오름차순 정렬한다.(array)
# 2. a1을 start에, b1을 end에 입력하고 저장한다.
# 3. 총 책을 나눠준 횟수를 저장할 result 변수와, 범위 내 개수를 저장할 count 변수를 1로 초기화한다.
# 4. 이후  array의 두번째 데이터부터 하나씩 탐색하며 start와 end의 범위 값이 달라질 때마다 이를 초기화해준다.
# 4-1. end - start + 1이 count보다 크다면 result의 값과 count의 값을 하나씩 더해준다.
# 4-2. start가 초기화될 때마다 초기화할 start에서 이전까지 저장해온 start를 뺀 값만큼 count에서 값을 뺀다.
def dfs(index_m, index_n):
    if visited[index_m][index_n]:
        return False
    visited[index_m][index_n] = True
    for j in graph[index_m]:
        if d[j] == 0 or dfs(index_m, j):
            d[j] = index_m
            visited[index_m][index_n] = True
            return True
    return False        


for tc in range(int(input())):
    n, m = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(m)]
    graph = [[] for _ in range(m+1)]
    visited = [[False for _ in range(n+1)] for _ in range(m+1)]
    d = [0 for _ in range(n+1)]
    for i in range(m):
        for j in range(array[i][1] - array[i][0] + 1):
            graph[i+1].append(array[i][0]+j)
    for i in range(m+1):
        dfs(i, 0)
    print(len(d) - d.count(0))
