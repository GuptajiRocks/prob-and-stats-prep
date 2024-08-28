stud = {0:5, 1:7, 2:10, 3:20, 4:12, 5:6}

mean = 0
for j in stud:
    mean = mean + (j*(stud[j]/60))

print(f"The mean for this case is {mean}")

tot = sum(stud.values())

def var(m):
    vari = 0
    for i in stud:
        vari = vari + (((i-m)**2)*(stud[i]/60))
    
    print(f"Variance for this case is {round(vari, 2)}")

var(mean)

def atl4():
    probs = 0
    for i in range(4,len(stud)):
        probs = probs + (stud[i]/60)
    
    print(f"Probability of atleast 4 is: {round(probs,2)}")

atl4()



