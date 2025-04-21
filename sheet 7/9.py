import numpy as np

a = np.arange(100).reshape(-1, 10)  

b = a[9][2]
print(b)