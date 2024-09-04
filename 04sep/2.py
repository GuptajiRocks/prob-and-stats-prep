import random
import numpy as np

xdat = [random.randint(1,100) for i in range(1,10)]
ydat = [random.randint(1,100) for j in range(1,10)]

xmean = ((sum(xdat))/len(xdat))
ymean = ((sum(ydat))/len(ydat))

N = len(xdat)
cov = 0
for i in range(N):
    cov = cov + ((xdat[i] - xmean)*(ydat[i] - ymean))

def calcmean():
    xmean = xdat.mean()
    ymean = ydat.mean()
    print(f"Mean of xdat is: {xmean}")
    print(f"Mean of ydat is: {ymean}")

sdl = []
def calcsd():
    sdx1 = 0
    for i in range(len(xdat)):
        sdx1 = sdx1 + (xdat[i] - xmean)
    
    sdx = (sdx1/len(xdat))**0.5
    print(f"Standard Deviation of xdat is: {sdx}")
    sdl.append(sdx)
    # gsdx = sdx

    sdy1 = 0
    for i in range(len(ydat)):
        sdy1 = sdy1 + (ydat[i] - ymean)
    
    sdy = (sdy1/len(ydat))**0.5
    print(f"Standard Deviation of ydat: {sdy}")
    sdl.append(sdy)
    # gsdy = sdy








