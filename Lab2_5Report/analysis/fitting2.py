# import math
#
# import pandas as pd
# import numpy as np
# from scipy.optimize import curve_fit
# import matplotlib.pyplot as plt
#
# # 读取Excel文件中的数据
# df = pd.read_excel('DataAnalysis.xlsx', sheet_name='加软管后')
# # df = pd.read_excel('DataAnalysis.xlsx')
#
# # 提取需要拟合的数据列
# # 将x_data和y_data转换为numpy数组
# x_data = np.array(df['f'])
# y_data = np.array(df['振动幅度/mm'])
#
#
# # 定义要拟合的函数模型
# def func(w, F_m, w0, beta):
#     return F_m/(np.sqrt((w0**2-w**2)**2+4*beta**2*w**2))
#
# # 使用curve_fit进行拟合
# popt, pcov = curve_fit(func, x_data, y_data)
#
# # 输出拟合参数
# print("拟合参数:", popt)
#
# x_plot = np.linspace(502.4, 503.4, num=1000)
#
# # 绘制拟合结果
# plt.figure()
# plt.scatter(x_data, y_data, label='$DataPoint$')
# plt.plot(x_plot, func(x_plot, *popt), 'r-', label='$Fitting$: $\\frac{F}{m}$=%5.3f, $w_0$=%5.3f$Hz$, $\\beta$=%5.3f' % tuple(popt))
#
# plt.xlabel('$f/Hz$', fontsize=16)
# plt.ylabel('$A/mm$', fontsize=16)
#
# plt.legend(fontsize='large')
# plt.show()



import math

import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# 读取Excel文件中的数据
df = pd.read_excel('DataAnalysis.xlsx', sheet_name='加软管后')

# 提取需要拟合的数据列
# 将x_data和y_data转换为numpy数组
x_data = np.array(df['f'])
y_data = np.array(df['振动幅度/mm'])


# 定义要拟合的函数模型
def func(w, F_m, w0, beta):
    return F_m/(np.sqrt((w0**2-(w)**2)**2+4*beta**2*(w)**2))

# 使用curve_fit进行拟合
popt, pcov = curve_fit(func, x_data, y_data)

# 输出拟合参数
print("拟合参数:", popt)

x_plot = np.linspace(502.4, 503.4, num=1000)

# 设置图像大小和分辨率
# plt.figure(figsize=(8.27, 11.69), dpi=300)  # A4纸大小，分辨率300dpi
plt.figure(figsize=(8.27, 11.69), dpi=150)  # A4纸大小，分辨率300dpi

# 绘制拟合结果
plt.scatter(x_data, y_data, label='$DataPoint$', s=10)  # 设置散点大小为10
plt.plot(x_plot, func(x_plot, *popt), 'r-', label='$Fitting$: $\\frac{F}{2\\pi m}$=%5.3f, $\\frac{w_0}{2\\pi}$=%5.3f$Hz$, $\\frac{\\beta}{2\\pi}$=%5.3f' % tuple(popt), linewidth=2)  # 设置线条粗细为2

plt.xlabel('$f/Hz$', fontsize=16)
plt.ylabel('$A/mm$', fontsize=16)

# plt.legend(fontsize='large')
plt.legend()

# plt.tight_layout()  # 调整布局使得所有元素显示完整

plt.savefig('fitting_plot.png')  # 保存图像为PNG格式文件
plt.show()
