# Task_08 Q_06:
# The number of tickets purchased by each student for the University X vs. University Y football game follows a distribution that has a mean of 2.4 and a standard deviation of 2.0.
# A few hours before the game starts, 100 eager students line up to purchase last-minute tickets. If there are only 250 tickets left, what is the probability that all 100 students will be able to purchase tickets?

import math

num_l_tic = float(input("Enter the number of last-minute tickets available at the box office: "))
num_Std = float(input("Enter the number of students waiting to buy tickets: "))
mu = num_Std * float(input("Enter the mean number of purchased tickets: "))
std = math.sqrt(num_Std) * float(input("Enter the standard deviation: "))

print(f"The probability that {num_Std} students can successfully purchase the remaining {num_l_tic}  tickets is: ",round(0.5*(1+math.erf((num_l_tic - mu)/(std * math.sqrt(2)))),4))