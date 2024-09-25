import matplotlib.pyplot as plt
s = [1,2,3,4,5,6]
jesus = {}

for i in s:
    jesus[i] = (s.count(i)/len(s))


for _ in jesus:
    print(f"The probability of {_} is {jesus[_]}")

plt.bar(s, list(jesus.values()))
plt.show()


