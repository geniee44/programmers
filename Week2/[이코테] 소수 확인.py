import sys
import math

def is_prime(x):
    tf = True
    for i in range(2, int(math.sqrt(x))):
        if x % i == 0:
            tf = False
            break
    
    return tf
