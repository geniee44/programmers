import sys
import math

n = int(input())
prime = [True] * (n + 1)

for i in range(2, n + 1):
    if prime[i]:
        j = 2
        for i * j <= n:
            prime[i * j] = False
            j += 1

for i in range(2, n + 2):
    if prime[i]:
        print(i, end=' ')
