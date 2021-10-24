# Task_08 Q_05:
# A large elevator can transport a maximum of 9800 pounds. Suppose a load of cargo containing 49 boxes must be transported via the elevator. The box weight of this type of cargo follows a distribution with a mean of 205 pounds and a standard deviation of 15 pounds. Based on this information, what is the probability that all 49 boxes can be safely loaded into the freight elevator and transported?

import math

max_w = int(input("Enter the maximum weight the elevator can transport: "))
n = int(input("Enter the number of boxes in the cargo: "))
mean_w = int(input("Enter the mean weight of a cargo box: "))
std = int(input("Enter its standard deviation: "))
mu_sum = n * mean_w 
sigma_sum = math.sqrt(n) * std

def CDF(x, mu, sigma):
    Z = (x - mu)/sigma
    return 0.5*(1 + math.erf(Z/(math.sqrt(2))))

print(f"The probability that the elevator can successfully transport all {n} boxes: ",round(CDF(max_w, mu_sum, sigma_sum), 4))