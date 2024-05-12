import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

from matplotlib.ticker import ScalarFormatter, FormatStrFormatter

# 从Excel文件中读取数据
# df = pd.read_excel('data1_24-05-09_0918.xlsx')
df = pd.read_excel('data1_24-05-09_0927.xlsx')

x = np.array(df['Untitled'])
y = np.array(df['Untitled 1'])

# 找到峰值
# peaks, _ = find_peaks(y, prominence=0.1, height=100)  # prominence参数可调整峰值的阈值

# 设置全局字号大小
plt.rcParams.update({
    'font.size': 12,
    'axes.titlesize': 20,
    'axes.labelsize': 24,
    'xtick.labelsize': 20,
    'ytick.labelsize': 20,
    'legend.fontsize': 20,
})

# 绘制图像
plt.figure(figsize=(9, 9))
plt.plot(x, y)
# plt.plot(x[peaks], y[peaks], "x")
plt.title('$V_L=1.5V$')
plt.xlabel('$V_{G_2K}/V$')
plt.ylabel('$I_P/10^{-12}A$')

# 在峰值旁边标注横纵坐标
# for i in peaks:
#     plt.text(x[i]-1, y[i]+3, f'({x[i]:.2f}, {y[i]:.2f})', color='red', ha='center')

plt.show()
