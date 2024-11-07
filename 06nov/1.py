import scipy.stats as stats
mu = 527
std = 112

def a(x):
    z = (x-mu)/std
    print(z)
    k = 1-stats.norm.cdf(z)
    per = k*100
    print(f"Probability of scoring more than 500 is: {round(per, 2)}%")

def b():
    Z = 1.645
    x = mu +(Z*std)
    print("To score in the top 5%, one needs to score more than: {}".format(x))


def c(x1, x2):
    z1 = (x1-mu)/std
    z2 = (x2-mu)/std
    k1 = 0
    k2 = stats.norm.cdf(z2)
    fink = (k2-k1)*100
    print(f"Probability is: {round(fink, 2)}%")

c(527, 554)