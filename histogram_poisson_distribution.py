from numpy import random
from matplotlib import pyplot

# Generates Random Poisson Distribution 
expectation_val = 5000
no_of_samples = 1000
data = random.poisson(expectation_val,no_of_samples)

# Prints the 1000 samples generated 
print(data)

# Generates a Histogram using the data generated
histogram = pyplot.hist(x, 50, facecolor='red', alpha=0.75)

# Labels & Titles for the Histogram
pyplot.ylabel('Probability')
pyplot.xlabel('Poisson Distribution')
pyplot.title(r'Random Histogram')

# Enables Grids on the Histogram Graph
pyplot.grid(True)

# Displays the Histogram
pyplot.show()
