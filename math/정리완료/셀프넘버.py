import sys
# 재귀함수로 풀 예정이기에 재귀 깊이 조정
sys.setrecursionlimit(10**6)

# 이전에 탐색했던 숫자가 나올 경우 이후 탐색하게될 숫자는 이전에 탐색한 숫자와 동일하기 때문에 탐색하지 않은 숫자들에 대해서만 탐색
# 이를 위해 방문 처리를 확인하기 위한 리스트 생성
visited = [False] * 10000

# 생성자 확인
def generator(n):
    # 주어진 n에 대해 d(n)을 계산
    result = n
    for i in range(len(str(n))):
        # 이때 n에 그대로 더할 경우 값이 변할 수 있으므로 다른 변수에 저장
        result += int(str(n)[i])

    # n이 10000 이상일 때 탐색 종료        
    if result > 10000:
        return
    
    # 아직 탐색하지 않은 숫자일 경우 탐색 
    elif visited[result-1] == False:      
        # 해당 숫자 방문 처리
        visited[result-1] = True
        generator(result)

# 1회부터 10000회까지 생성자 함수 실행
for i in range(1, 10000):
    generator(i)    

# 방문하지 않은 값 출력
for i in range(10000):
    if visited[i] == False:
        print(i+1)
