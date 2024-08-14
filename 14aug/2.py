l = [20,20,21,21,21,22,23,26,27,27]

def checkprob(arr, check):
    tot = len(arr)
    fav = arr.count(check)
    prob = fav/tot
    print(f"Probability is: {prob}")



l1 = ['a','a','b','b','c','x','y','z','z','z']
check = str(input("Enter string to check: "))

checkprob(l1,check)



