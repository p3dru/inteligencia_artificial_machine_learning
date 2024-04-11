import pandas as pd
import numpy as np

#cria um DataFrame com valores faltantes
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, 7, 8],
    'C': [9, 10, 11, np.nan]
})

#coloca a média dos dados nos locais vazios
df.fillna(df.mean(), inplace=True)

print(df)