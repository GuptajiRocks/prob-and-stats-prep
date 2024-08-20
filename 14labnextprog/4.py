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
  print(probabilities)

  
#   heads_counts = {}
#   for outcome, prob in probabilities.items():
#     heads_count = outcome.count('H')
#     if heads_count not in heads_counts:
#       heads_counts[heads_count] = 0
#     heads_counts[heads_count] += prob

#   print("Probabilities for tossing", num_coins, "coins:")
#   for heads_count, prob in heads_counts.items():
#     print(f"{heads_count} heads: {prob}")