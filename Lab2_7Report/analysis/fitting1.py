import math

import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# 读取Excel文件中的数据
df = pd.read_excel('data1.xlsx', sheet_name='T')
# df = pd.read_excel('DataAnalysis.xlsx')

# 提取需要拟合的数据列
# 将x_data和y_data转换为numpy数组
x_data = np.array(df['表面温度']) + 273.15
y_data = np.array(df['辐射传感器电压/mV'])


# 定义要拟合的函数模型
# def func(T, sigma, bias_1, bias_2):
#     return sigma*(T+bias_1)**4+bias_2

def func(T, sigma, bias_2):
    return sigma*(T)**4+bias_2

# 使用curve_fit进行拟合
popt, pcov = curve_fit(func, x_data, y_data)

# 输出拟合参数
print("拟合参数:", popt)

x_plot = np.linspace(0, 400, num=1000)

# 绘制拟合结果
plt.figure()
plt.scatter(x_data, y_data, label='$DataPoint$')
# plt.plot(x_plot, func(x_plot, *popt), 'r-', label='$Fitting$: $\\sigma$=%5.3f , bias_1=%5.3f , bias_2=%5.3f ' % tuple(popt))

plt.plot(x_plot, func(x_plot, *popt), 'r-', label='$Fitting$: k=%5.3e ,  bias_2=%5.3f ' % tuple(popt))

plt.xlabel('T/K', fontsize=20)
plt.ylabel('U/mV', fontsize=20)

plt.legend(fontsize='large')
plt.show()
