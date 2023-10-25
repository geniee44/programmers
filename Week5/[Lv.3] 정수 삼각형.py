from collections import deque
def solution(triangle):
    answer = 0
    n = sum([i for i in range(1, len(triangle) + 1)])
    dp = [[0] * i for i in range(1, len(triangle) + 1)]
    q = deque()
    q.append((0, 0, 0))
    
    while q:
        idx, loc, w = q.popleft()
        dp[idx][loc] = max(dp[idx][loc], w + triangle[idx][loc])
        
        if idx == len(triangle) - 1:
            continue
                
        if 0 <= loc < len(triangle[idx]):
            q.append((idx + 1, loc + 1, dp[idx][loc]))
            q.append((idx + 1, loc, dp[idx][loc]))
        
    return max(dp[len(triangle) - 1])
