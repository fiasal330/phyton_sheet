import numpy as np
a = np.arange(100).reshape(-1, 10)
row3 = a[2, :]
print(row3)