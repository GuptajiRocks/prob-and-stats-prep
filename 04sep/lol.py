import numpy as np

def generate_random_numbers_numpy(num_numbers, min_value, max_value):
  """Generates a list of random integers within a specified range using NumPy.

  Args:
    num_numbers: The number of random numbers to generate.
    min_value: The minimum value of the random numbers.
    max_value: The maximum value of the random numbers.

  Returns:
    A NumPy array of random integers.
  """

  random_numbers = np.random.randint(min_value, max_value + 1, size=num_numbers)
  return random_numbers

if __name__ == "__main__":
  num_numbers = 80
  min_value = 1
  max_value = 100
  random_numbers = generate_random_numbers_numpy(num_numbers, min_value, max_value)
  print(random_numbers)