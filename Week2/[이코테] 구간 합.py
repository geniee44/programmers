import sys
n = int(input())

data = list(map(int, input().split(' ')))

sum = 0
prefix = [0]

for i in data:
    sum += i
    prefix.append(sum)

left, right = map(int, input().split(' '))

print(prefix[right] - prefix[left - 1])
