import sys

def quick_sort(start, end, list):
    if start >= end:
        return
    
    pivot = start
    left = start + 1
    right = end
    
    while left <= right:
        while list[left] < list[pivot] and left <= end:
            left += 1
        while list[right] > list[pivot] and right >= start:
            right -= 1
        
        if left > right:
            list[right], list[pivot] = list[pivot], list[right]
        else:
            list[left], list[right] = list[right], list[left]
    
    quick_sort(start, right - 1, list)
    quick_sort(right + 1, end, list)

def quick_sort_python(list):
    if len(list) <= 1:
        return list
    
    pivot = list[0]
    tail = list[1:]
    
    left_list = [x for x in tail if x < pivot]
    right_list = [x for x in tail if x > pivot]
    
    return quick_sort_python(left_list) + pivot + quick_sort_python(right_list)
        
quick_sort(0, len(list) - 1, list)
quick_sort_python(list)
