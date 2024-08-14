import numpy as np
import random
random.seed(50)

mol = ["I","am","Studying", "in", "BU"]
arr = random.choices(mol, k = 1500)
print(arr)
sample = []
for i in range(len(arr)):
    if arr[i] == "BU":
        try:
            sample.append(arr[i+1])
        except Exception:
            continue


freqsample = dict()

for i in sample:
    if i in freqsample:
        freqsample[i] += 1
    else:
        freqsample[i] = 1

print(freqsample)

