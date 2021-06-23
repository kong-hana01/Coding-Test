'''
문제
국가의 역할 중 하나는 여러 지방의 예산요청을 심사하여 국가의 예산을 분배하는 것이다. 국가예산의 총액은 미리 정해져 있어서 모든 예산요청을 배정해 주기는 어려울 수도 있다. 그래서 정해진 총액 이하에서 가능한 한 최대의 총 예산을 다음과 같은 방법으로 배정한다.

모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정한다. 상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정한다. 
예를 들어, 전체 국가예산이 485이고 4개 지방의 예산요청이 각각 120, 110, 140, 150이라고 하자. 이 경우, 상한액을 127로 잡으면, 위의 요청들에 대해서 각각 120, 110, 127, 127을 배정하고 그 합이 484로 가능한 최대가 된다. 

여러 지방의 예산요청과 국가예산의 총액이 주어졌을 때, 위의 조건을 모두 만족하도록 예산을 배정하는 프로그램을 작성하시오.


입력
첫째 줄에는 지방의 수를 의미하는 정수 N이 주어진다. 
N은 3 이상 10,000 이하이다. 다음 줄에는 각 지방의 예산요청을 표현하는 N개의 정수가 빈칸을 사이에 두고 주어진다. 이 값들은 모두 1 이상 100,000 이하이다. 그 다음 줄에는 총 예산을 나타내는 정수 M이 주어진다. M은 N 이상 1,000,000,000 이하이다. 


출력
첫째 줄에는 배정된 예산들 중 최댓값인 정수를 출력한다. 

'''

import sys
n = int(sys.stdin.readline()) # 지방 수 입력
budget_list = list(map(int, sys.stdin.readline().split())) # 각 지방별 예산 입력
max_budget = int(sys.stdin.readline()) # 지원 가능한 총 예산 입력
budget_list.sort() # 총 예산 정렬

start_value = 0 # 최소한의 예산
end_value = budget_list[n-1] # 각 지방의 예산 중 최대 예산
result = 0 # 지원가능한 예산의 최대값 초기화

while start_value <= end_value: # 최소한의 예싼이 각 지방의 예산 중 최대 예산보다 커질 때까지 반복
    mid_value = (start_value+end_value) // 2 # 현재 주어진 범위 내에서의 중간값 예산
    total_budget = sum([x if mid_value >= x else mid_value for x in budget_list]) # 중간값 예산보다 클 경우 중간 값으로 바꾸고, 작을 경우는 그대로 내버려둔 뒤, 이를 합한 예산
    
    # 위에서 구한 예산과 지원가능한 총 예산이 같다면 mid_value를 입력받고 끝낸다.
    if total_budget == max_budget:
        result = mid_value
        break

    # 위에서 구한 예산이 지원가능한 총 예산보다 크다면 mid_value - 1을 end_value로 입력한다.
    elif total_budget > max_budget:
        end_value = mid_value - 1
    # 위에서 구한 예산이 지원가능한 총 예산보다 작다면 mid_value + 1을 start_value로 두고, 이때의 mid_value와 result 중 큰 값을 result에 저장한다.
    else:
        result = max(result, mid_value)
        start_value = mid_value+1

print(result)