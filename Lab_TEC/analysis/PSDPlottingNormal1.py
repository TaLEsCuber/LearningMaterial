import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import welch
import numpy as np

# 读取Excel文件中的数据
file_path = 'P_3.xlsx'  # 请将此路径替换为你的Excel文件路径

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

# 创建一个子图
fig, ax = plt.subplots(figsize=(16, 8))

# 绘制PSD图
ax.plot(frequencies, psd, label='PSD')
ax.set_xlabel('Frequency (Hz)', fontsize=20)
ax.set_ylabel('PSD ($K^2/Hz$)', fontsize=20)
ax.set_title('Power Spectral Density', fontsize=20)
ax.legend(fontsize=20)
ax.grid(True, which='both', linestyle='--')
ax.tick_params(axis='both', which='major', labelsize=18)

# 调整布局以防止标题和标签重叠
plt.tight_layout(pad=3.0)

# 展示图像
plt.show()
