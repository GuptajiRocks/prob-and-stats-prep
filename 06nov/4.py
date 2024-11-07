import scipy.stats as st
mu = 75
std = 25
n = 110

newstd = std/(n**0.5)
l = 82 

z = (l-mu)/newstd

fs = st.norm.cdf(z)
fin = 1-fs
print(f"The probability that BU students exceed phone usage time of {l} minutes is: {round((fin*100), 2)}%")