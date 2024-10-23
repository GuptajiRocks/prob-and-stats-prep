pa = 0.4
pb = 0.6
m1 = 2

x = 1
a = 0
b = 5

ptl1a = 1-(2.7**((-1*1)/m1))
ptl1b = (x-a)/(b-a)

ptl1 = (ptl1a*pa)+(ptl1b*pb)

pawtl1 = (ptl1a*pa)/(ptl1)

print(pawtl1)
