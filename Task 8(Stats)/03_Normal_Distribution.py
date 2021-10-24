# Task_08 Q_03:
# In a certain plant, the time taken to assemble a car is a random variable, x, having a normal distribution with a mean of 20 hours and a standard deviation of 2 hours. What is the probability that a car can be assembled at this plant in:

# Less than 19.5 hours?
# Between 20 and 22 hours?

import math

def CDF(x, mean, std):
    return 1/2*(1+math.erf((x-mean) / std / 2**(1/2)))

mean = 20
std = 2
print("The probability that a car can be assembled in less than 19.5 hours: ",round(CDF(19.5, mean, std), 3))
print("The probability that a car can be assembled in between 20 to 22 hours: ",round(CDF(22, mean, std) - CDF(20, mean, std), 3))