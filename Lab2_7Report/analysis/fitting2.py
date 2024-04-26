import math

import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# 读取Excel文件中的数据
df = pd.read_excel('data1.xlsx', sheet_name='D')
# df = pd.read_excel('DataAnalysis.xlsx')

# 提取需要拟合的数据列
# 将x_data和y_data转换为numpy数组
x_data = np.array(df['距离/mm'])
y_data = np.array(df['辐射传感器电压/mV'])


# 定义要拟合的函数模型
# def func(T, sigma, bias_1, bias_2):
#     return sigma*(T+bias_1)**4+bias_2

def func(d, k, bias_1, bias_2):
    return k*(d - bias_1)**(-2)+bias_2


initial_guess = [1000, 40.0, 0.06]
# 使用curve_fit进行拟合
popt, pcov = curve_fit(func, x_data, y_data, p0=initial_guess)

# 输出拟合参数
print("拟合参数:", popt)

x_plot = np.linspace(100, 400, num=1000)

# 绘制拟合结果
plt.figure()
plt.scatter(x_data, y_data, label='$DataPoint$')
# plt.plot(x_plot, func(x_plot, *popt), 'r-', label='$Fitting$: $\\sigma$=%5.3f , bias_1=%5.3f , bias_2=%5.3f ' % tuple(popt))

plt.plot(x_plot, func(x_plot, *popt), 'r-', label='$Fitting$: k=%5.3e ,  bias_1=%5.3f mm, bias_2=%5.3f mV' % tuple(popt))

plt.xlabel('d/mm', fontsize=20)
plt.ylabel('U/mV', fontsize=20)

plt.legend(fontsize='large')
plt.show()