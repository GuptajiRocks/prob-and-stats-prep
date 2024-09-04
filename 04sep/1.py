import random
# import numpy as np
# l = np.arange(random.randint(1,100))
xdat = [random.randint(1,100) for i in range(1,10)]
ydat = [random.randint(1,100) for j in range(1,10)]

xmean = (sum(xdat))/len(xdat)
ymean = (sum(ydat))/len(ydat)

N = len(ydat)

print(f"The mean of xdat is {xmean}")
print(f"The mean of ydat is {ymean}")

cov = 0

for i in range(len(xdat)):
    cov = cov + ((xdat[i] - xmean)*(ydat[i] - ymean))

fincov = cov / (N-1)

print(f"Covariance is: {fincov}")

sdx1 = 0
sdy1 = 0

for i in range(len(xdat)):
    sdx1 = sdx1 + (xdat[i] - xmean)

sdx = (sdx1/len(xdat))**0.5

for j in range(len(ydat)):
    sdy1 = sdy1 + (ydat[j] - ymean)

sdy = (sdy1/len(ydat))**0.5

pmf = fincov/(sdx*sdy)
print(f"Peason Correlation Coeffecient is: {pmf}")

# print(xdat)