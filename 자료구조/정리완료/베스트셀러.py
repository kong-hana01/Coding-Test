# https://www.acmicpc.net/problem/1302
# 접근방법
# 딕셔너리를 통해 책 개수를 체크한 뒤, 가장 많이 팔린 책의 이름을 출력한다.
n = int(input())
books = {}
for _ in range(n):
    book = input()
    if book not in books.keys():
        books[book] = 0
    books[book] += 1
maxCount = 0
sortedBooks = sorted(books.items(), key=lambda x: x[0])
for key, value in sortedBooks:
    if maxCount < value:
        maxCount = value
        result = key
print(result)