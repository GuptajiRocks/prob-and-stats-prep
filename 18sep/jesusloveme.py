import numpy as np
import random
random.seed(150)

mean = 12
std_dev = 19
sample_size = 8500

random_numbers = np.random.normal(loc=mean, scale=std_dev, size=sample_size)

standard_normal_numbers = (random_numbers - mean) / std_dev

p1min = mean-(0.325*std_dev)
p1max = mean+(0.325*std_dev)

within_range = np.sum((standard_normal_numbers >= p1min) & (standard_normal_numbers <= p1max))
percentage_within_range = (within_range / sum(random_numbers)) * 100

print(f"Percentage of numbers between {p1min} and {p1max}: {percentage_within_range:.3f}%")
