# https://www.acmicpc.net/problem/1543
# 접근 방법 
# 전체 문서의 문자를 하나씩 탐색하며 만약 검색하고 싶은 단어의 첫글자와 같다면 검색하고 싶은 단어의 인덱스도 하나씩 증가시키며 비교한다.
# 이때 검색하고 싶은 단어를 모두 탐색했는데 검색하고 싶은 단어와 동일하다면 이를 하나씩 카운트한다.

# 문서의 길이는 최대 2500이므로 길지 않기에 리스트로 변환하지 않고, 문자열로 처리한다.

# document = [x for x in input()] # 인덱싱을 통한 반복을 위해 리스트 형태로 문서 입력
document = input()
voca = input() # 검색하고 싶은 단어 입력

# count = 0 # 중복되지 않게 단어가 등장한 횟수 초기화
# voca_index = 0 # 검색하고 싶은 단어의 인덱스 초기화

# # 문서 탐색
# for x in document:

#     # 찾고자 하는 문자와 현재 문서에서 탐색 중인 문자가 같은 경우 voca_index += 1
#     if voca[voca_index] == x:
#         voca_index += 1


#     else:
#        voca_index = 0
    
#     # 검색하고자 하는 단어의 인덱스가 단어의 길이와 같아질 때 count +1, voca_index 초기화
#     if voca_index == len(voca):
#         count += 1
#         voca_index = 0


# print(count)


# 접근 방법 2
# 문자열의 길이가 2500까지이므로 현재 탐색하고자하는 문서의 길이만큼 매번 탐색을 진행한다.
start_index = 0
end_index = len(voca)
count = 0

while end_index <= len(document):
    if voca == ''.join(document[start_index:end_index]):
        count += 1
        start_index += len(voca)
        end_index += len(voca)
    else:
        start_index += 1
        end_index += 1

print(count)

# 접근방법 3
# count함수를 사용한다.
print(document.count(voca))