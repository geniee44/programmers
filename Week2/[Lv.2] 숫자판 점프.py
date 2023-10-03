def dfs(v, visited, x, y, sum, cnt):
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0. 0]
    
    if cnt == 5 :
        if visited[sum] == False:
            visited[sum] = True
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(v, visted, nx, ny, sum * 10 + v[nx][ny], cnt + 1)
    
    return


def solution(n):
    answer = 0
    visited = [0] * 1000000
    
    for i in range(5):
        for j in range(5):
            dfs(v, visited, i, j, v[i][j], 0)
    
    for i in range(1000000):
        if visited[i] == 1:
            answer += 1
        
    return answer

