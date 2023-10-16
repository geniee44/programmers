from collections import deque

def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    
    q = deque([(0, 0, 1)])
    
    while q:
        x, y, dist = q.popleft()
        if x == n - 1 and y == m - 1:
            return dist
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append((nx, ny, dist + 1))
    
    return -1
        
