# https://www.acmicpc.net/problem/1072
# 접근방법 1
# 현재 z를 저장하고 총 게임 횟수와 이긴 횟수를 증가시키며 z와 달라진 점이 있는지 확인한다.
# 이때 달라진다면 총 증가시킨 횟수를 출력한다.
# 하지만 시간복잡도 초과로 인해 문제 해결을 못함 (총 게임 횟수: 10억, z는 98인 경우 시간 내에 해결 불가)
# 접근방법 2
# 총 게임 횟수가 최대 10억이기에 z가 변할 수 있는 게임 횟수의 최대는 10억개이다.
# (가장 보수적으로 생각하면 10억개에서 이긴 횟수가 9억 8천만개라면 z=98, 이를 99로 바꾸기 위해선 10억번을 더 해야한다. z=99인 경우는 문제 해결 불가능)
# 따라서 1부터 10억까지 이진탐색을 진행하면서 탐색 중인 값을 주어진 총 횟수와 증가시킨 횟수에 더해가며 계산한다.
# 시간복잡도 : O(logN)
x, y = map(int, input().split())
z = int(100 * y / x )
# z = int(y/x * 100) # 실수 오차로 인해 틀린 답
start = 1
end = 1000000000
result = 1000000001
while start <= end:
	mid = (start + end) // 2
	total = x + mid
	win = y + mid
	z_ = int(100 * win/total) 
	if z_ > z: # 승률을 올리는 경우
		result = min(result, mid)
		end = mid - 1 # end값을 줄여서 이진탐색 재 진행
	else:
		start = mid + 1 # 승률이 그대로인 경우 start 값을 올려섯 이진탐색 재 진행
		
if result == 1000000001:
	print(-1)
else:
	print(result)
	# print('z:', z)
	# print('z_:', (y+result)/(x+result) * 100)