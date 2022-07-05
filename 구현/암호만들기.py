# https://www.acmicpc.net/problem/1759
# 접근 방법
# 주어진 조건대로 만들 수 있는 암호를 모두 만들어 출력한다.
def check(letter):
    cnt_vowel = 0
    for vowel in ['a', 'e', 'i', 'o', 'u']:
        if vowel in letter:
            cnt_vowel+=1
    if 0 < cnt_vowel and 2 <= l-cnt_vowel:
        return True
    return False

def make_password(i, letter):
    if len(letter) == l:
        if check(letter):
            result.append(letter)
        return 
    for idx in range(i, c):
        make_password(idx+1, letter+letters[idx])
    

l, c = map(int, input().split())
letters = input().split()
letters.sort()
result = []
for i in range(c):
    make_password(i+1, letters[i])
for pw in result:
    print(pw)