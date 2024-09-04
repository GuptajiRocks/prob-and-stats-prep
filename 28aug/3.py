x = 2000

dd = {1:0.3, 2:0.4, 3:0.2, 4:0.1}
dk = list(dd.keys())

arrvall = []
for i in dd:
    arrvall.append(int(dd[i]*2000))

fulla = []
print(arrvall)
count = 0
for i in arrvall:
    for j in range(i):
        fulla.append(dk[count])
    
    count += 1



