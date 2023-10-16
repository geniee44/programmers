def solution(numbers, target):
    idx = curr = 0

    def dfs(numbers, target, curr, idx):
        if idx == len(numbers):
            if curr == target:
                return 1
            else:
                return 0

        return dfs(numbers, target, curr + numbers[idx], idx + 1) \
                + dfs(numbers, target, curr - numbers[idx], idx + 1)

    answer = dfs(numbers, target, idx, curr)
    return answer
