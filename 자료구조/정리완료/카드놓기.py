# https://www.acmicpc.net/problem/5568
# 접근 방법
# k개 만큼 수를 뽑아 정수를 만들어 이를 set에 넣고 모든 정수만들기가 끝났을 때 set의 길이를 출력한다.
def create_int(integer, count, checkList):
    if count > k:
        Integer.add(int(integer))
        return
    for i in range(n):
        if i not in checkList:
            create_int(integer + cards[i], count+1, checkList + [i])

n = int(input())
k = int(input())
cards = [input() for _ in range(n)]
Integer = set([])
create_int('', 1, [])
print(len(Integer))