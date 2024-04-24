import math

import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# 读取Excel文件中的数据
df = pd.read_excel('data1.xlsx', sheet_name='绿光')
# df = pd.read_excel('DataAnalysis.xlsx')

# 提取需要拟合的数据列
# 将x_data和y_data转换为numpy数组
x_data = np.array(df['θ'])
y_data = np.array(df['I/muW'])


# 定义要拟合的函数模型
def func(theta, I_0, phi_0, C):
    return I_0*(np.cos(theta/57.3+phi_0))**2+C

# 使用curve_fit进行拟合
popt, pcov = curve_fit(func, x_data, y_data)

# 输出拟合参数
print("拟合参数:", popt)

x_plot = np.linspace(0, 100, num=1000)

# 绘制拟合结果
plt.figure()
plt.scatter(x_data, y_data, label='$DataPoint$')
plt.plot(x_plot, func(x_plot, *popt), 'r-', label='$Fitting$: $I_0$=%5.3f $\\mu W$, $\\phi_0$=%5.3f rad, $C$=%5.3f $\\mu W$' % tuple(popt))

plt.xlabel('$\\theta/\\degree$', fontsize=16)
plt.ylabel('$I_{\\theta}/\\mu W$', fontsize=16)

plt.legend(fontsize='large')
plt.show()
