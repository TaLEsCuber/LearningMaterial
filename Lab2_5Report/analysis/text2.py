import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# 从Excel文件中读取数据
df = pd.read_excel('DataAnalysis.xlsx', sheet_name='加软管后')

# 假设Excel文件中有两列数据，分别是x和y
x_data = np.array(df['f'])
y_data = np.array(df['振动幅度/mm'])

# 使用三次样条插值
f = interp1d(x_data, y_data, kind='cubic')
x_smooth = np.linspace(x_data.min(), x_data.max(), 500)
y_smooth = f(x_smooth)

# 画图
plt.figure()
plt.plot(x_smooth, y_smooth)
plt.scatter(x_data, y_data)
plt.show()
