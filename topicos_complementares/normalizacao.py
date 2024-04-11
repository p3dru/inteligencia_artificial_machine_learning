from sklearn.preprocessing import MinMaxScaler, StandardScaler
import numpy as np

#dados de exemplo
data = np.array([[10, 20], [30, 40], [50, 60]])

#normalização Min-Max
scaler_min_max = MinMaxScaler()
data_min_max = scaler_min_max.fit_transform(data)
print("Normalização Min-Max:\n", data_min_max)

#normalização Z-Score
scaler_z_score = StandardScaler()
data_z_score = scaler_z_score.fit_transform(data)
print("Normalização Z-Score:\n", data_z_score)
