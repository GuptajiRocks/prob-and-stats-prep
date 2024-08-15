import itertools

def coin_toss_probabilities(num_coins):
  

  outcomes = list(itertools.product(['H', 'T'], repeat=num_coins))
  total_outcomes = len(outcomes)

  probabilities = {}
  for outcome in outcomes:
    probabilities[outcome] = 1 / total_outcomes

  return probabilities

if __name__ == "__main__":
  num_coins = 4
  probabilities = coin_toss_probabilities(num_coins)

  print("Probabilities for tossing", num_coins, "coins:")
  for outcome, probability in probabilities.items():
    print(f"{outcome}: {probability}")