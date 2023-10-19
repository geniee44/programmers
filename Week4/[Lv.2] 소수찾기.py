import math, itertools

def solution(numbers):
    answer = []
    array = [int(i) for i in numbers]
    candidate = []
    
    # 순열 조합 itertools의 permutations 사용
    for i in range(1, len(array) + 1):
        candidate += list(itertools.permutations(array, i))
    
    def check_num(n):
        tf = True
        if n == 0 or n == 1: return False
        if n == 2: return True
        
        # 소수 찾을 때 제곱근+1까지 범위 설정
        for l in range(2, int(math.sqrt(n)) + 1):
            if n % l == 0:
                tf = False
                break
        return tf
    
    for per in candidate:
        num = 0
        for i in range(len(per)):
            num += per[i] * math.pow(10, i)
                
        if check_num(num) and num not in answer: answer.append(num)
    
    return len(answer)
