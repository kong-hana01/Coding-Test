def dfs(i, r, c, dist, places, visited):
    if 0 < dist <= 2 and places[i][r][c] == 'P':
        return True
    elif dist == 2 or places[i][r][c] == 'X':
        return False
    
    visited[r][c] = True
    for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        if 0<=r+dr<=4 and 0<=c+dc<=4 and not visited[r+dr][c+dc] and dfs(i, r+dr, c+dc, dist+1, places, visited):
            return True
    return False

def check(i, places):
    for r in range(5):
        for c in range(5):
            if places[i][r][c] == 'P':
                visited = [[False for _ in range(5)] for _ in range(5)]
                check = dfs(i, r, c, 0, places, visited)
                if check:
                    return 0
    return 1

def solution(places):
    answer = []
    for i in range(5):
        result = check(i, places)
        answer.append(result)
    return answer