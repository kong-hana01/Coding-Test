# 접근방법
# i까지의 최적의 해를 구하기 위해 i-1번째 창고와, i-2번째 창고까지의 최적의 해만을 사용한다.
# 따라서 다이나믹 프로그래밍을 활용하면 해결할 수 있다.

import sys
# 정수 N 입력 받기
n = int(sys.stdin.readline())
# 모든 식량 정보 입력 받기
warehouse = list(map(int, sys.stdin.readline().split()))

# n은 3이상
# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0 for _ in range(n)]


# 다이나믹 프로그래밍 진행(바텀업)
d[0] = warehouse[0] # 첫번째 창고에서의 최댓값
d[1] = max(d[0], warehouse[1]) # 두번쨰 창고까지의 최댓값
for i in range(2, n):
    d[i] = max(d[i-2]+warehouse[i], d[i-1])    

# 계산된 결과 출력
print(d[n-1])