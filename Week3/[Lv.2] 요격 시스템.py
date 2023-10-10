def solution(targets):
    answer = 0
    start = 0

    for s, e in sorted(targets):
        if start > s:
            start = min(start, e)
        else:
            start = e
            answer += 1

    return answer
