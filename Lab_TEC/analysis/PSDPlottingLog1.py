import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import welch
import numpy as np

# 读取Excel文件中的数据
file_path = 'PID_2.xlsx'  # 请将此路径替换为你的Excel文件路径

# 使用pandas读取Excel文件
data = pd.read_excel(file_path)

# 假设你的数据有两列，分别是时间和温度
time = data['时间 - 曲线 0']
temperature = data['幅值 - 曲线 0']

# 计算采样频率
dt = np.mean(np.diff(time))
fs = 1 / dt

# 计算PSD
frequencies, psd = welch(temperature, fs=fs)

# 设置输出图像的大小
plt.figure(figsize=(12, 4))  # 宽12英寸，高4英寸

# 绘制PSD图
plt.loglog(frequencies, psd, label='PSD')

# 设置横纵轴标签，标题和图例的字号大小
plt.xlabel('Frequency (Hz)', fontsize=20)
plt.ylabel('PSD ($K^2/Hz$)', fontsize=20)
plt.title('Power Spectral Density', fontsize=20)
plt.legend(fontsize=20, loc='upper right')  # 设置图例的字号并放置在右上角

# 设置横纵坐标轴刻度标签的字号
plt.xticks(fontsize=24)
plt.yticks(fontsize=24)

# 自动调整布局
plt.tight_layout()

plt.grid(True, which='both', linestyle='--')

# 保存图像，保持长宽比例不变
plt.savefig('psd_plot.png', bbox_inches='tight')

plt.show()
