# https://www.acmicpc.net/problem/16953
# 접근방법
# 연산 조건에 따라 queue에 값을 삽입하고 빼면서 값을 키로 하고 연산 횟수를 밸류로 하는 딕셔너리를 활용하여 만든다.

from collections import deque

a, b = map(int, input().split()) # a, b 입력
count_dic = {a:1} # 연산횟수 계산용 딕셔너리
queue = deque([]) # 연산횟수 계산을 위한 queue
queue.append(a)
result = -1 # 결과값 초기화

while queue: # queue가 없어질때까지 반복
    x = queue.popleft() 
    if int(str(x) + str(1)) < b: # x에서 뒤에 1을 더한 값이 b보다 작은 경우
        queue.append(int(str(x) + str(1))) # 이를 queue에 삽입하고
        count_dic[int(str(x) + str(1))] = count_dic[x] + 1 # 연산횟수를 딕셔너리에 저장한다.

    elif int(str(x) + str(1)) == b: # x에서 뒤에 1을 더한 값이 b와 같은 경우
        result = count_dic[x]+1 # result에 값을 입력하고 
        break # 반복문을 종료한다.

 
    if x * 2 < b: # x * 2가 b보다 작은 경우
        queue.append(x*2) # 이를 queue에 삽입하고
        count_dic[x*2] = count_dic[x] + 1 # 연산횟수를 딕셔너리에 저장한다.

    elif x * 2 == b: # x * 2가 b와 같은 경우
        result = count_dic[x]+1 # result에 값을 입력하고 
        break # 반복문을 종료한다.

print(result) # 결과 값 출력