# 접근방법
# 주어진 레고의 길이 리스트를 주어진 x의 절반을 기준으로 나누어 리스트(short_lego, long_lego)에 저장한 뒤, 이를 각각 오름차순 정렬한다.
# 단 정확히 x의 절반이 되는 레고가 두 개라면 해당 레고는 바로 정답 리스트(result)에 저장한다.
# 이후 short_lego와 long_lego의 길이가 더 짧은 걸 기준으로 하나씩 탐색한다.(최적화를 위해) 그리고 나머지 레고에 대해 이진탐색을 진행하며 탐색 중인 두 길이가 x와 같다면 정답 리스트(result)에 저장해준다.
# 모든 탐색이 끝나고 result를 확인하며 abs(x[0] - x[1])이 가장 큰 값을 출력한다.
# 단위: 10**7 나노미터 = 1cm


import sys
input = sys.stdin.readline

while True:
    try:
        x = int(input())
        n = int(input())
        lego = [int(input()) for _ in range(n)]
        x_ = x * (10 ** 7)
        short_lego = []
        mid_lego = []
        long_lego = []
        result = []

         
        for l in lego:
            if l > x_ // 2:    
                long_lego.append(l)
            elif l < x_ // 2:
                short_lego.append(l)
            else:
                result.append([l, l])
    
        long_lego.sort()
        short_lego.sort()

        if len(short_lego) <= len(long_lego):
            for lego1 in short_lego:
                start = 0
                end = len(long_lego) - 1
                while start <= end:
                    mid = (start + end) // 2
                    lego2 = long_lego[mid]
            
                    if lego1 + lego2 < x_:
                        start = mid + 1
                    elif lego1 + lego2 > x_:
                        end = mid - 1
                    else:
                        result.append([lego1, lego2])
                        break
            
        else:
            for lego1 in long_lego:
                start = 0
                end = len(short_lego) - 1
                while start <= end:
                    mid = (start + end) // 2
                    lego2 = short_lego[mid]
            
                    if lego1 + lego2 < x_:
                        start = mid + 1
                    elif lego1 + lego2 > x_:
                        end = mid - 1
                    else:
                        result.append([lego2, lego1])
                        break
    
        result.sort(key=lambda x: abs(x[1] - x[0]), reverse = True)
        if result:
            print('yes', result[0][0], result[0][1])
        else:
            print('danger')
    except:
        break
