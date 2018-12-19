import statistics
from random import randint

import cubed


data = [randint(60,100) for _ in range(100)]
variance = statistics.variance(data)
print(data)
print("The variance is", variance)


print("The cube of 8 is", cubed.cubed(8))

