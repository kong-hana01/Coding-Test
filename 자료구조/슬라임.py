import heapq, sys
input = sys.stdin.readline

for tc in range(int(input())):
    n = int(input())
    slime = []
    for x in list(map(int, input().split())):
        heapq.heappush(slime, x)
    
    energy = 1
    while len(slime) != 1:
        x1 = heapq.heappop(slime)
        x2 = heapq.heappop(slime)
        new_slime = x1 * x2
        heapq.heappush(slime, new_slime)
        energy = energy * (new_slime % 1000000007)
        energy %= 1000000007
    print(energy % 1000000007)