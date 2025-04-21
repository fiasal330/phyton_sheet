import numpy as np
a = np.arange(100).reshape(-1, 10)

#to duble 

a = np.arange(100).reshape(-1, 10).astype(np.float64)
print(a)