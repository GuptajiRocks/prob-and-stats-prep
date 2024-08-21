import itertools

def coin_toss_probabilities(num_coins):
  outcomes = list(itertools.product(['H', 'T'], repeat=num_coins))
  return outcomes
cc = 0
num_coins = int(input("Enter the number of coins: "))
probs = coin_toss_probabilities(num_coins)
prob_c = 0
print("For which do you want to calculate probability -> (H/T)?: ")
sidechoice = str(input("Enter: "))
if sidechoice == ('H' or 'h'):
  print(f"Enter the number of {sidechoice} you want probability of: ")
  coinc = int(input("Enter the value: "))
  cc = coinc
  for i in probs:
    if i.count('H') == coinc:
      prob_c +=1
else:
  print("Invalid input") 


total = num_coins**2

print(f"The probability for {cc}, {sidechoice} coins simultaneously is: {cc/total}")







