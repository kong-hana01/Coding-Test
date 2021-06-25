import sys
k, n = map(int, sys.stdin.readline().split())
lan_lines = [int(sys.stdin.readline()) for _ in range(k)]

start = 0
end = max(lan_lines)
length = 0
while True:
    if start > end: 
        break
    mid = (start+end) // 2
    if mid == 0:
        if length == 0:
            length = 1
        break
    count_of_cutting_lan_lines = [x // mid for x in lan_lines if x > 0]
    total = sum(count_of_cutting_lan_lines)
    if total < n:
        end = mid-1
    else:
        start = mid+1
        length = mid
        
print(length)