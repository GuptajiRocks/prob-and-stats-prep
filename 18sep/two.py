x = [0.25, 0.65, 0.10, 0.50, 0.80, 0.30, 0.70, 0.40, 0.20, 0.60]
mx = max(x)
mix = min(x)

print(f"Maximum Value is {mx}")
print(f"Minimum value is {mix}")
print(f"Probility func: {1/(mx-mix)}")
print(f"Mean is: {(mx+mix)/2}")
print(f"Variance is: {((mx-mix)**2)/12}")


def cdf():
    tp = 0
    for i in x:
        if (i < mix):
            print(f"Prob({i}) = {0}")
            tp = tp + 0
        elif (i >= mix and i <= mx):
            print(f"Prob({i}) = {(i-mix)/(mx-mix)}")
            tp = tp + (i-mix)/(mx-mix)
        elif (i > mx):
            print("Prob is 1")
            tp = tp+1
    
    print(f"Gradual CDF: {tp}")

cdf()


