import math

def solution(r1, r2):
    answer = 0
    answer = []
    for a in range(1, r2 + 1):
        for b in range(0, c):
            if r1 ** 2 <= a ** 2 + b ** 2 <= r2 ** 2:
                answer += 1
    answer *= 4
    
    return answer


from math import floor, ceil, pow, sqrt

def solution(r1, r2):
    count_per_quadrant = 0
    for x in range(1, r2 + 1):
        max_y = floor(sqrt(pow(r2, 2) - pow(x, 2)))
        min_y = ceil(sqrt(pow(r1, 2) - pow(x, 2))) if r1 > x else 0
        count_per_quadrant += max_y - min_y + 1

    return count_per_quadrant * 4
