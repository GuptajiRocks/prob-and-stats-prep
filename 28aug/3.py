x = 2000

dd = {1:0.3, 2:0.4, 3:0.2, 4:0.1}
dk = list(dd.keys())

arrvall = []
for i in dd:
    arrvall.append(int(dd[i]*2000))
fullar=[]
for i in arrvall:
    for j in range(i):
        fullar.append(dk[i])

print(fullar)

