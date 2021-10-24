# Task_08 Q_04:
# The final grades for a Physics exam taken by a large group of students have a mean of 70 and a standard deviation of 10. If we can approximate the distribution of these grades by a normal distribution, what percentage of the students:

# Scored higher than 80 (i.e., have a grade>80)?
# Passed the test (i.e., have a grade>=60)?
# Failed the test (i.e., have a grade<60)?
# Find and print the answer to each question on a new line, rounded to a scale of 2 decimal places.

import math
mean, std = 70, 10
CDF = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))
print("The percentage of students having grade>80: ",round((1-CDF(80))*100,2))
print("The percentage of students having grade>=60: ",round((1-CDF(60))*100,2))
print("The percentage of students having grade<60: ",round((CDF(60))*100,2))