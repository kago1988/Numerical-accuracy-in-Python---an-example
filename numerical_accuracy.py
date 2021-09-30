import numpy as np


print(0.1+0.1+0.1)
# output: 0.30000000000000004


temp = np.add(0.1,0.1)
temp = np.add(temp,0.1)
print(temp)
# output: 0.30000000000000004


print(round(0.1, 1) + round(0.1, 1) + round(0.1, 1))
# output: 0.30000000000000004


print(round(0.1 + 0.1 + 0.1, 1))
# output: 0.3