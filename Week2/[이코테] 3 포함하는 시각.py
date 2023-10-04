def solution(n):
    # 완전 탐색
    count = 0
    
    for i in range(n + 1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k):
                    count += 1
        
    return count
  
