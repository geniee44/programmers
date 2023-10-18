def solution(begin, target, words):
    n = len(words)
    w = len(begin)
    visited = [-1 for _ in range(n)]
    
    def bfs(now, count):
        if now == target:
            return count
        for i in range(n):
            if visited[i] == -1:
                same = 0
                for j in range(w):
                    if now[j] == words[i][j]:
                        same += 1
                if same == w - 1:
                    visited[i] = count + 1
                    result = bfs(words[i], count + 1)
                    if result != 0:
                        return result
        return 0
    
    if target not in words:
        return 0
    
    return bfs(begin, 0)
