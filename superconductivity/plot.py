import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

tempIncrease = pd.read_csv('升温.csv')
voltInT = tempIncrease['样品两端电压(mV)']
voltInTemp = tempIncrease['铂温度计两端电压(mV)']
r = voltInT / 1
temp = (-3.9083e-3 + np.sqrt(-3.9083e-3 * -3.9083e-3 - 40 * -5.7577e-7 * (0.1 - 0.001 * voltInTemp))) / (2 * (-5.7577e-7))
fig, ax = plt.subplots()
ax.scatter(temp, r)
ax.plot(temp, r)
ax.set_xlabel('温度/T', family = ['Source Han Sans CN'])
ax.set_ylabel('电阻/$\Omega$', family = ['Source Han Sans CN'])
plt.show()