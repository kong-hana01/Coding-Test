# 접근 방법
# 1. 집과 사무실의 길이 차이가 최대 d 이내여야지 철로를 놓을 수 있는 대상이 된다. 따라서 리스트 컴프리핸션 정렬을 사용해 대상이 되는 데이터만 따로 정리하고 정렬해 리스트(array)를 만든다.
# 2. 새로 만든 리스트의 개수에 맞게 dp 테이블을 초기화하고, 가장 시작점이 낮은 순서대로 인덱스를 매긴다. 이때 각 인덱스의 원소는 [같은 시작점을 가진 데이터의 개수, 그 시작점부터 d까지 포함되는 데이터 개수]로 설정한다.
# 3. array를 하나씩 탐색하면서 시작 점 값을 저장하고, dp에  각 원소를 하나씩 추가한다.
# 4. array를 탐색하다가 이전 시작 점 값과 같은 경우 같은 시작점을 가진 데이터의 개수를 하나 늘려준다.
# 5. 이후 dp 테이블에서 최대값을 출력한다.

# 스위핑 알고리즘 배우고 재도전!

import sys
n = int(sys.stdin.readline()) # n 입력
array = [list(map(int, sorted(sys.stdin.readline().split()))) for _ in range(n)] # 집과 사무실 위치 입력
d = int(sys.stdin.readline())
array = [x for x in array if abs(x[0] - x[1]) <= d] # array 내 데이터 중 집과 사무실의 거리가 d 이내인 경우만 저장
array.sort(key=lambda x:x[0]) # array 내 데이터 최소값으로 정렬

if array:
    start = array[0][0]
    end = array[0][1] 
    i_1 = 0
    i_2 = 0
    i_a = 0

    dp = [[0, 0] for _ in range(len(array))]
    dp[0] = [1, 1]

    
    for x in array[1:]: # array의 데이터를 하나씩 탐색
        print(dp)
        if start == x[0]: # 이전의 저장한 start가 같은 경우 dp 테이블의 저장중인 i_1에 1을 더한다.
            dp[i_1][0] += 1 
        elif start != x[0]: # 이전에 저장한 start가 x[0]과 다른 경우 dp 테이블의 인덱스를 옮기고 해당 인덱스의 첫번째 원소를 1로 바꾼다.
            i_1 += 1
            dp[i_1][0] += 1
            start = x[0]
        
        end = x[1] # 가장 거리가 먼 것으로 저장
        print('end: ', end)
        print('array[i_a]: ', array[i_a])
        if end - array[i_a][0] <= d: # 현재 주어진 데이터들을 모두 포괄할 수 있는 길이라면 dp[i_2][1]에 값 누적
            dp[i_2][1] += 1
            
        else: # 현재 주어진 데이터들을 모두 포괄할 수 있는 길이가 아니라면 해당 길이가 될 때까지 아래 동작을 반복
            while end - array[i_a][0] > d:
                count = dp[i_2][1] - dp[i_2][0] # dp 테이블에서 i_1의 시작점이 같은 데이터의 개수를 제외한 해당 길이에서부터 d로 포괄가능한 길이의 데이터 개수
                i_a += dp[i_2][0] # array 인덱스 증가
                i_2 += 1 # dp 테이블 인덱스 증가
                dp[i_2][1] = count + 1 # dp 테이블의 누적합 입력

    print(max(dp, key=lambda x: x[1])[1]) # 최종적으로 누적된 dp 테이블의 값 중 가장 높은 값 출력
else:
    print(0)