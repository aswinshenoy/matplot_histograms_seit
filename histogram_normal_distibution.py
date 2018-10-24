from numpy import random
from matplotlib import pyplot

# Generates Random Normal (Gaussian) Distribution 
mean = 5000
std_deviation = 1
no_of_samples = 1000
data = random.normal(mean,std_deviation,no_of_samples)

# Prints the 1000 samples generated 
print(data)

# Generates a Histogram using the data generated
histogram = pyplot.hist(data, 50, facecolor='red', alpha=0.75)

# Labels & Titles for the Histogram
pyplot.ylabel('Probability')
pyplot.xlabel('Gaussian/Normal Distribution')
pyplot.title(r'Histogram from Random Normal Distirbution')

# Enables Grids on the Histogram Graph
pyplot.grid(True)

# Displays the Histogram
pyplot.show()
