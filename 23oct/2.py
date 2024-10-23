import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def simulate_and_plot(population_size, sample_size, num_samples):

    population = np.random.uniform(0, 100, population_size)

    sample_means = []
    for _ in range(num_samples):
        sample = np.random.choice(population, sample_size, replace=False)
        sample_means.append(np.mean(sample))


    plt.hist(sample_means, bins=30, density=True, alpha=0.6)

    mean = np.mean(population)
    std_dev = np.std(population) / np.sqrt(sample_size)
    x = np.linspace(min(sample_means), max(sample_means), 100)
    y = norm.pdf(x, mean, std_dev)
    plt.plot(x, y, color='red', lw=3, label=f'Normal Distribution (μ={mean:.2f}, σ={std_dev:.2f})')

    plt.xlabel('Sample Mean')
    plt.ylabel('Density')
    plt.title(f'Distribution of Sample Means (Sample Size: {sample_size})')
    plt.legend()
    plt.show()

population_size = 10000
sample_size = 30
num_samples = 10000

simulate_and_plot(population_size, sample_size, num_samples)