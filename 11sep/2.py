pdef = 0.02
# P(x = k) = (1-p)**(k-1) * p
k = 7
pmf = ((1-pdef)**(k-1))*pdef
print(pmf)

exp = 1/pdef
print(exp)