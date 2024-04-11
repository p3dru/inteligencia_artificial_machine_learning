import pandas as pd
import numpy as np
from statsmodels.tsa.arima_model import ARIMA
import matplotlib.pyplot as plt

#gera uma série temporal simples
np.random.seed(0)
data = np.random.randn(100)
dates = pd.date_range(start='1/1/2020', periods=100)
series = pd.Series(data, index=dates)

#plota a série temporal
plt.plot(series)
plt.show()

#modela a série temporal com ARIMA
model = ARIMA(series, order=(5,1,0))
model_fit = model.fit(disp=0)

#plota a previsão do modelo
plt.plot(series)
plt.plot(model_fit.fittedvalues, color='red')
plt.title('Previsão com ARIMA')
plt.show()
