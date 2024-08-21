# import numpy as np
r = 30
b = 20
g = 10
tot = r+b+g

# Drawing red ball

def p_red():
    print(r/tot)

def p_blue():
    print(b/tot)

def condi():
    pborg = (b+g)/tot
    pb = b/tot
    print(pb/pborg)
