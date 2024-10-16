def prob(lam, t):
    ft = ((2.7)**(lam*t*-1))
    return ft

morethan3 = prob(2, 3)
# probability of P(T>3 | T>2) = P(T>1)

morethan1 = prob(2, 1)
print(morethan3)
print(morethan1)