lam1 = 0.0003
def expoprob(lam, t):
    ft = (2.7)**((lam*-1*t))
    return ft

lam2 = 0.00035
whenlam1 = expoprob(lam1, 10000)
whenlam2 = expoprob(lam2, 10000)

print(whenlam1)
print(whenlam2)

if (whenlam2 < whenlam1):
    print("No effect")
else:
    print("Redesign will affect output")