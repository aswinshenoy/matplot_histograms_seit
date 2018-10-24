# Histogram using Matplotlib on Python
Histograms generated using matplotlib library on Python based on random samples generated using numpy library.

**Requires** *Python 3 with matplotlib and numpy installed*

## Histogram of Poisson Distribution
A poisson distribution with 1000 samples is generated randomly using `numpy.random.poisson` function of the numpy library. The function takes two parameters - expectation value (λ) for the distribution, and the number of samples to be generated, and returns an array containing the samples.

These samples are then ploted into a histogram using `pyplot.hist` function of the matplotlib library.

## Histogram of Gaussian/Normal Distribution
A gaussian/normal distribution with 1000 samples is generated randomly using `numpy.random.normal` function of the numpy library. The function takes three parameters - the mean of the distribution, the standard deviation (width) of the distribution and the number of samples to be generated, and returns an array containing the samples.

These samples are then ploted into a histogram using `pyplot.hist` function of the matplotlib library.
