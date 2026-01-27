import numpy as np
a = np.array([1,2,3]); b = np.array([4,5,6])
print("Sum:", a+b, "Product:", a*b)
print("Mean of a:", np.mean(a), "Max of b:", np.max(b))
c = a.reshape(3,1); print("Reshaped a:\n", c)
