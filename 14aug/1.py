# import numpy as np
import random
n = int(input("Enter seed val: "))
random.seed(n)

l = [random.randint(92,105) for i in range(0,1500)]
print(l)

freq = dict()

for i in l:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
sum = 0
for i in freq:
    sum += freq[i]
print(freq)
print(sum)
