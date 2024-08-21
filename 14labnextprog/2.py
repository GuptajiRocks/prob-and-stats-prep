import itertools

def coin_toss_probabilities(num_coins):
  

  outcomes = list(itertools.product(['H', 'T'], repeat=num_coins))
  total_outcomes = len(outcomes)

  probabilities = {}
  for outcome in outcomes:
    probabilities[outcome] = 1 / total_outcomes

  return probabilities

num_coins = int(input("Enter the number of coins: "))

probs = coin_toss_probabilities(num_coins)
print(probs)
