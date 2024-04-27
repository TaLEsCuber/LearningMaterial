import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

# 设置全局字号大小和图像尺寸
plt.rcParams.update({
    'font.size': 12,
    'axes.titlesize': 20,
    'axes.labelsize': 24,
    'xtick.labelsize': 20,
    'ytick.labelsize': 20,
    'legend.fontsize': 20,
    'figure.figsize': (8.27, 11.69)
})



# 读取Excel文件中的数据
df = pd.read_excel('data1.xlsx', sheet_name='D')
# df = pd.read_excel('DataAnalysis.xlsx')

# 提取需要拟合的数据列
# 将x_data和y_data转换为numpy数组
x_data = np.array(df['距离/mm'])
y_data = np.array(df['辐射传感器电压/mV'])


# 定义要拟合的函数模型
def func(d, k, R, d_0, C):
    return k*(np.sin(np.arctan(R/(d-d_0))))**2+C


initial_guess = [100, 20, 40.0, 0.06]
# 使用curve_fit进行拟合
popt, pcov = curve_fit(func, x_data, y_data, p0=initial_guess)

# 计算相关系数
residuals = y_data - func(x_data, *popt)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((y_data - np.mean(y_data))**2)
r_squared = 1 - (ss_res / ss_tot)

# 输出拟合参数和相关系数
print("拟合参数:", popt)
print("相关系数:", r_squared)

x_plot = np.linspace(100, 350, num=1000)

# 绘制拟合结果
plt.figure()
plt.scatter(x_data, y_data, label='$DataPoint$')

# 在图例中显示相关系数
legend_label = '$Fitting$: k=%5.3e, R=%5.3f mm, $d_0$=%5.3f mm,\n C=%5.3fmV, $R^2$=%.6f' % (*popt, r_squared)
plt.plot(x_plot, func(x_plot, *popt), 'r-', label=legend_label)

plt.xlabel('d/mm')
plt.ylabel('U/mV')

plt.legend()
plt.show()
