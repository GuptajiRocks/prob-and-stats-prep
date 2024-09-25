import matplotlib.pyplot as plt
import numpy as np

# Define the possible outcomes
x = np.arange(1, 7)

# Define the PMF values
pmf = np.repeat(1/6, 6)

# Create the plot
plt.figure(figsize=(8, 6))
plt.stem(x, pmf)
plt.xlabel('Outcome (x)')
plt.ylabel('Probability (P(X = x))')
plt.title('PMF of Rolling a Fair Six-Sided Die')
plt.xticks(x)
plt.ylim([0, 0.2])  # Adjust y-axis limits for better visualization
plt.grid(True)
plt.show()