n = int(input())
count = 0
for i in range(1, n+1):
    # 한자리수 ~ 두자리수는 모두 등차수열로 구성이 가능하다.
    if i <= 99:
        count += 1
    # 세자리수는 자릿수로 구분해 등차수열임을 확인한다.
    elif i <= 999:
        third = int(str(i)[0])
        second = int(str(i)[1])
        first = int(str(i)[2])
        if second - first == third - second:
            count += 1
    # 네자리수는 1000밖에 없고, 이는 등차수열이 아니기에 이를 생략한다.
print(count)