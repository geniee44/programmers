def solution(n, plans):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    move = {'R': 0, 'L': 1, 'D': 2, 'U': 3}
    x, y = 1, 1
    
    for plan in plans:
        nx = x + dx[move[plan]]
        ny = y + dy[move[plan]]
        
        if nx < 1 or nx > n or ny < 1 or ny > n:
            continue
        else:
            x = nx
            y = ny
    
    return x, y

