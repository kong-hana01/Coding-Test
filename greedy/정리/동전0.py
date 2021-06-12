n, k = map(int, input().split())
for i in range(n):
    if i == 0:
        coin_list = [int(input())]
    else:
        coin_list.append(int(input()))

# 접근 방식 1
def count_coin(k, count=0, n=n):
    if k > coin_list[n-1]:
        return count_coin(k-coin_list[n-1], count+1, n)
    elif k < coin_list[n-1]:
        return count_coin(k, count, n-1)
    elif k == coin_list[n-1]:
        return count + 1
print(count_coin(k))


# 접근 방식 2
def count_coin_2(k, count=0, n=n):
    m, d = divmod(k, coin_list[n-1])
    if d == 0:
        return count + m
    return count_coin_2(k-m*coin_list[n-1], count+m, n-1)

print(count_coin_2(k))