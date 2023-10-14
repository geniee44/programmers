def solution(brown, yellow):
    answer = []
    blocks = brown + yellow
    a = 2
    while True:
        a += 1
        if blocks % a == 0:
            b = blocks // a
            if (a + b) * 2 - 4 == brown:
                answer.append(b)
                answer.append(a)
                break
    return answer
