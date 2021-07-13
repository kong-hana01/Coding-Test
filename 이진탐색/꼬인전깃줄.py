# https://www.acmicpc.net/status?user_id=gksqlsl11&problem_id=1365&from_mine=1
# 접근 방법
# 증가하는 부분수열로 로직을 작성한 뒤, N에서 가장 큰 값을 빼준다.
# 현재 탐색하는 수보다 앞에 있는 수 중 작은 수의 개수 + 1을 인덱스로 하는 리스트의 값에 작은 값을 입력한다.
n = int(input())
array = list(map(int, input().split()))
d = [n+1] * (n+1) # dp 테이블 초기화 / 인덱스 = 부분수열의 개수, 값 = 그 개수에 해당하는 전봇대 번호 중 더 작은 수 
d[1] = array[0]
for x in array[1:]:
    # 이진탐색 진행
    start = 1
    end = n + 1
    index = 0
    while start <= end:
        mid = (start + end) // 2
        if d[mid] < x: # 탐색 중인 수가 mid개의 부분수열을 가진 어떤 수보다 크다면
            index = max(index, mid)
            start = mid + 1
        else:
            end = mid - 1
    # 현재 찾은 부분수열의 개수 인덱스의 값에 이를 저장(항상 탐색 중인 수는 다음 인덱스보다 작을 수밖에 없음)
    d[index + 1] = x
    # print(d)
for i in range(1, n + 1):
    if d[i] == n + 1: # i : 부분 수열의 개수 + 1
        break
print(n - (i - 1)) # 현재 주어진 전봇대의 수 - 부분 수열의 개수