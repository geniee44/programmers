from collections import deque

def solution(sequence, k):
    answer = []

    candidate = []
    q = deque()
    q.append(sequence[0])
    i = 0

    while True:
        if sum(q) > k:
            if len(q) == 1:
                i += 1
                q.append(sequence[i])
            q.popleft()
        elif sum(q) < k:
            i += 1
            if i == len(sequence):
                break
            q.append(sequence[i])
        else:
            candidate.append((len(q), i))
            q.popleft()

    candidate.sort()
    
    answer.append(candidate[0][1] - candidate[0][0] + 1)
    answer.append(candidate[0][1])

    return answer
