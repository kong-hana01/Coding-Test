# https://www.acmicpc.net/problem/2212
# 접근방법
# 주어진 센서의 좌표를 오름차순으로 정렬한 뒤, 센서간의 거리를 리스트에 저장한다.
# 거리를 오름차순으로 정렬한 뒤, 집중국의 개수 - 1만큼 리스트에서 값이 큰 순서대로 뺀다.
# 이후 남은 리스트의 합을 구한다.

n = int(input()) # 센서의 개수 입력
k = int(input()) # 집중국의 개수 입력
array = list(map(int, input().split())) # 센서의 좌표 입력
array.sort() # 센서의 좌표 오름차순 정렬

distance = [] # 좌표간의 거리를 저장할 리스트 초기화
x_1 = array[0] 
for x_2 in array[1:]:
    distance.append(x_2 - x_1) # 좌표간의 거리 저장
    x_1 = x_2
distance.sort() # 좌표간의 거리 오름차순으로 정렬
print(sum(distance[:n-1-(k-1)])) # 거리가 가장 많은 것을 집중국의 개수 - 1만큼 뺀 뒤, 남은 거리를 합하여 이를 출력