# h를 최대로 하는 m만큼의 떡을 집에 가져가기 위해선 h가 주어질 때 h보다 큰 떡들과 h와의 차이의 합이 m이 되어야한다.
# 따라서 h보다 긴 길이의 떡과 h의 차이의 합이 m이 되는 지점을 이진탐색으로 찾고 이를 반환하면 된다.
import sys
sys.setrecursionlimit(10**6)


# 내 코드
n, m = 4, 9 # 떡의 개수, 요청한 떡의 길이
heights_of_rice_cakes = [19, 15, 10, 17] # 떡의 길이
heights_of_rice_cakes.sort()

def binary_search(start, end, m):

    mid = (start+end)//2 # 주어진 크기의 중간 값을 h로 한다.

    long_heights_of_rice_cakes = [x-mid for x in heights_of_rice_cakes if mid < x]  # 중간 지점의 떡 길이보다 긴 떡 배열
    heights_sum = sum(long_heights_of_rice_cakes)

    # 절단기로 자른 떡들의 합이 손님이 필요한 m보다 큰 경우
    if heights_sum > m:
        # 절단기의 높이를 더 키워서 heights_sum를 줄여야하기때문에 시작점을 높인다.
        if mid+1 < end:
            return binary_search(mid+1, end, m)
        # 만약 mid+1이 end보다 큰 경우에 mid를 반환한다. -> 최적의 mid값을 반환하지 못할 수 있음 
        else:
            return mid

    # 절단기로 자른 떡들의 합이 손님이 필요한 m보다 작은 경우 절단기의 높이를 줄여서 heights_sum를 높여야하기때문에 끝점을 줄인다.
    elif heights_sum < m:
        return binary_search(start, mid-1, m)

    # 절단기로 자른 떡들의 합이 손님이 필요한 m과 같은 경우 m을 출력한다.
    else:
        return mid

# 시작점은 0부터 시작, 끝점은 떡의 길이 중 가장 높은 것으로 한다.
print(binary_search(0, heights_of_rice_cakes[-1], m))




# 이코테 모범답안
n, m = map(int, input().split())
array = list(map(int, input().split()))
start = 0
end = max(array)

result = 0
while (start <= end):
    total = 0
    mid = (start+end) // 2
    for x in array:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로 여기서 result 기록
        start = mid + 1

# 정답 출력
print(result)