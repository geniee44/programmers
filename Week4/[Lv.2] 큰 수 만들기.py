def solution(number, k):
    stack = []
    
    for num in number:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    
    # If there are still remaining 'k' to be removed, remove from the end
    while k > 0:
        stack.pop()
        k -= 1
    
    return ''.join(stack)

