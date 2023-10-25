from collections import deque
def solution(triangle):
    answer = 0
    dp = [[0] * i for i in range(1, len(triangle) + 1)]
    dp[0][0] = triangle[0][0]
    
    for x in range(1, len(triangle)):
        for y in range(len(triangle[x])):
            if y == 0:
                dp[x][y] = dp[x - 1][y] + triangle[x][y]
            elif y == len(triangle[x]) - 1:
                dp[x][y] = dp[x - 1][y - 1] + triangle[x][y]
            else:
                dp[x][y] = max(dp[x - 1][y - 1], dp[x - 1][y]) + triangle[x][y]

    return max(dp[len(triangle) - 1])

