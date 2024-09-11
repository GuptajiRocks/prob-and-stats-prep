def fact(n):
    if n <= 1:
        return 1
    else:
        return n*fact(n-1)

# 3 bulbs to be drawn, so X can take 4 values, 0,1,2,3
# 4 defective bulbs, so 6 good ones.
# p(X=r) = nCr * (png)**r * (pg)**(n-r)

probfuse = 4/10
probgood = 1-probfuse



px0 = (fact(3)/(fact(0)*fact(3-0)))*(probfuse**0)*(probgood**3)
px1 = (fact(3)/(fact(1)*fact(3-1)))*(probfuse**1)*(probgood**2)
px2 = (fact(3)/(fact(2)*fact(3-2)))*(probfuse**2)*(probgood**1)
px3 = (fact(3)/(fact(3)*fact(3-3)))*(probfuse**3)*(probgood**0)

print(px0,px1, px2, px3)