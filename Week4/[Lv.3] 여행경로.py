from collections import deque

def solution(tickets):
    answer = []
    q = deque()
    q.append(("ICN", ["ICN"], []))
    
    while q:
        airport, path, used = q.popleft()
        
        if len(tickets) == len(used):
            answer.append(path)
        
        for idx, country in enumerate(tickets):
            if airport == country[0] and idx not in used:
                q.append((country[1], path + [country[1]], used + [idx]))
    
    answer.sort()
    
    return answer[0]
