from collections import deque

def solution(n, computers):
    answer = 0
    visited = []
    q = deque()
    
    for a in range(n):
        if a not in visited:
            q.append(a)
            answer += 1
            
            while q:
                now = q.popleft()
                for i in range(n):
                    if computers[now][i] == 1 and i not in visited:
                        visited.append(i)
                        q.append(i)   
    
    return answer
