import random
import numpy as np

n = int(input("Enter seed: "))
random.seed(n)

mol = ["I", "am", "writing", "a", "program"]

arr = random.choices(mol, k=1500)
freq = dict()


for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)
