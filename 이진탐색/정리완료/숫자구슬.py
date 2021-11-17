# https://www.acmicpc.net/problem/2613
# 접근 방법
# 현재 주어진 숫자 구슬의 모든 합을 end로, 구슬의 최댓값을 start로 하는 이진탐색을 한다.
# 구슬을 하나씩 탐색하며 숫자를 합해가다 mid보다 숫자가 커지면 숫자의 합계를 초기화하고 그룹을 하나 더 늘려간다.
# 이후 만들어진 그룹의 개수를 비교해 m과 같은 경우 mid를 .결과값으로 저장해가며 최소가 되는 길이를 찾는다.
n, m = map(int, input().split())
marble = list(map(int, input().split()))
start = max(marble)
end = sum(marble)
min_max_value = sum(marble)
while start <= end:
    mid = (start+end) // 2
    total = 0
    count_marble = 0
    count_ = []
    for i in range(n):
        if marble[i] + total > mid:
            total = 0
            count_.append(count_marble)
            count_marble = 0
            
        elif n - i < m - len(count_):
            total = 0
            count_.append(count_marble)
            count_marble = 0
            
        total += marble[i]
        count_marble += 1
        
    if count_marble:
        count_.append(count_marble)
        
    count_group = len(count_)
    if count_group == m:
        if min_max_value >= mid:
            min_max_value = mid
            result = count_
        end = mid - 1
        
    elif count_group > m:
        start = mid + 1
        
    else:
        end = mid - 1

print(min_max_value)
for x in result:
    print(x, end=' ')