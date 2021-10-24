# Task_08 Q_01:
# The ratio of boys to girls for babies born in Russia is 1.09:1. If there is 1 child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys?
# Write a program to compute the answer using the above parameters. Then print your result, rounded to a scale of 3 decimal places (i.e., 1.234 format).

import math

p = 1.09/(1+1.09)
res = 0
for i in range(3):
    res += math.factorial(6) / math.factorial(i) / math.factorial(6-i) * p**i * (1-p)**(6-i)
Answer = round(1-res, 3)
print(Answer)
