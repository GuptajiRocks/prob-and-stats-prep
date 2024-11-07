import numpy as np
import matplotlib.pyplot as plt

# Set the sample size and number of simulations
sample_size = 40
num_simulations = 1000

# 1. Normal Distribution
normal_means = []
for _ in range(num_simulations):
    sample = np.random.normal(18, 20, sample_size)
    sample_mean = np.mean(sample)
    normal_means.append(sample_mean)

# 2. Poisson Distribution
poisson_means = []
for _ in range(num_simulations):
    sample = np.random.poisson(10, sample_size)
    sample_mean = np.mean(sample)
    poisson_means.append(sample_mean)

# 3. Exponential Distribution
exponential_means = []
for _ in range(num_simulations):
    sample = np.random.exponential(1/20, sample_size)
    sample_mean = np.mean(sample)
    exponential_means.append(sample_mean)

# Plot the histograms of the sample means
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.hist(normal_means, bins=30, density=True)
plt.title('Normal Distribution')

plt.subplot(1, 3, 2)
plt.hist(poisson_means, bins=30, density=True)
plt.title('Poisson Distribution')

plt.subplot(1, 3, 3)
plt.hist(exponential_means, bins=30, density=True)
plt.title('Exponential Distribution')

plt.tight_layout()
plt.show()