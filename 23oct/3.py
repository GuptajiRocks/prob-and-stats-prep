import numpy as np
import matplotlib.pyplot as plt

population_size = 1000
mean = 75
std_dev = 10

scores = np.random.normal(mean, std_dev, population_size)

proportion_above_80 = np.sum(scores > 80) / population_size

x = np.linspace(mean - 3 * std_dev, mean + 3 * std_dev, 1000)

pdf = 1 / (std_dev * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - mean) / std_dev) ** 2)

plt.plot(x, pdf, label='Normal Distribution')

shaded_area = np.sum(pdf[scores > 80])
plt.fill_between(x[scores > 80], 0, pdf[scores > 80], color='gray', alpha=0.3, label=f'Proportion Above 80% ({proportion_above_80:.2f})')

plt.xlabel('Scores')
plt.ylabel('Probability Density')
plt.title('Normal Distribution of Student Scores (Mean=75, SD=10)')

plt.legend()

plt.grid(True)
plt.show()