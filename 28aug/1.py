outcomes = []
for i in range(1,9):
    for j in range(1,9):
        for k in range(1,9):
            for l in range(1,9):
                outcomes.append((i,j,k,l))

l = [i for i in range(4,33)]
print(l)
print(outcomes)

probd = dict()

for i in l:
    count = 0
    for j in outcomes:
        if (sum(j) == i):
            count += 1
    
    probd[i] = count/len(outcomes)


for _ in probd:
    print(f"The probability of {_} is: {probd[_]}")