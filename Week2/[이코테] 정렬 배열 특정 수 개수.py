from bisect import left_bisect, right_bisect

n, x = map(int, input().split(' '))
array = list(map(int, input().split()))

def count_by_range(array, i, j):
    left_num = left_bisect(array, i)
    right_num = right_bisect(right, j)
    
    return right_num - left_num

count = count_by_range(array, x, x)

if count == 0:
    result = -1
else:
    result = count

print(result)
