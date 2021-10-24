# Task_08 Q_02:
# A manufacturer of metal pistons finds that, on average, 12% of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of 10 pistons will contain:

# No more than 2 rejects?
# At least 2 rejects?

import math

p = 0.12
ans1 = 0
for i in range(0, 3):
    ans1 += math.factorial(10)/math.factorial(i)/math.factorial(10-i) * p**i * (1-p)**(10-i)
    if i == 1:
        ans2 = 1 - ans1
print(round(ans1, 3))
print(round(ans2, 3))