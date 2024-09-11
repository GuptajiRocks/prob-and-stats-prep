import math
hsal = [10,15,20,25,30]
fr = [2,3,4,3,2]

mean = 0

def fact(n):
    if n<=1:
        return 1
    else:
        return n*fact(n-1)

for i in range(len(hsal)):
    mean = mean + (hsal[i]*fr[i])


mean = mean/sum(fr)

# Exactly 20 sold
px20 = (mean**20)*((math.exp(-mean)))/fact(20)
print(f"Mean crossiants sold per hour: {mean}")
print(f"The standard deviation is: {(mean**0.5)}")
print(f"Exactly 20 sold probability is: {px20}")

