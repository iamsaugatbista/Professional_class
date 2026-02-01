from sklearn.preprocessing import StandardScaler
import numpy as np 
import numpy as np

X = np.array([[1, 2],
              [3, 4],
              [5, 6]])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print(X_scaled)