pbdwb = 0.93
pnbwnb = 0.88
pbr = 0.03
pnb = 1-pbr
pbrwnb = 1 - pnbwnb 

pbd = (pbdwb*pbr) + (pbrwnb*pnb)
print(pbd)
pbrwbd = (pbdwb * pbr)/pbd

print(round(pbrwbd,4))