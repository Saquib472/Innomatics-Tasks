# Task_08 Q_07:
# You have a sample of 100 values from a population with mean 500 and with standard deviation 80. Compute the interval that covers the middle 95% of the distribution of the sample mean; in other words, compute A and B such that P(A<x<B)=0.95. Use the value of z=1.96. Note that z is the z-score.

mu, sigma = 500, 80
muS, sigmaS = mu, sigma/(100**0.5)
A = mu - (1.96*sigmaS)
B = mu + (1.96*sigmaS)

print(round(A,2))
print(round(B,2))