# 접근방법
# 각 비행기마다 도킹할 수 있는 게이트 중 가장 뒷번호의 게이트에 도킹하면 된다.
# 단, 리스트 인덱스를 통해 도킹을 시도하면 최대 약 5,000,050,000번까지 연산을 해야하기에 set() 자료 구조와 in 연산자를 이용해 도킹을 해보려한다.
# set 자료구조에서의 in 시간복잡도 : O(1)
import sys
g = int(sys.stdin.readline())
p = int(sys.stdin.readline())
airplane = [[] for _ in range(p+1)]

for i in range(1, p+1):
    int(sys.stdin.readline()) 
