import math

import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# 读取Excel文件中的数据
df = pd.read_excel('DataAnalysis.xlsx', sheet_name='加软管前')
# df = pd.read_excel('DataAnalysis.xlsx')

# 提取需要拟合的数据列
# 将x_data和y_data转换为numpy数组
x_data = np.array(df['f'])
y_data = np.array(df['振动幅度/mm'])


# 定义要拟合的函数模型
def func(w, F_m, w0, beta):
    return F_m/(np.sqrt((w0**2-w**2)**2+4*beta**2*w**2))

# 使用curve_fit进行拟合
popt, pcov = curve_fit(func, x_data, y_data)

# 输出拟合参数
print("拟合参数:", popt)

x_plot = np.linspace(503.5, 504.5, num=1000)

# 绘制拟合结果
plt.figure()
plt.scatter(x_data, y_data, label='$DataPoint$')
plt.plot(x_plot, func(x_plot, *popt), 'r-', label='$Fitting$: $\\frac{F}{m}$=%5.3f, $w_0$=%5.3f$Hz$, $\\beta$=%5.3f' % tuple(popt))

plt.xlabel('$f/Hz$', fontsize=16)
plt.ylabel('$A/mm$', fontsize=16)

plt.legend(fontsize='large')
plt.show()
