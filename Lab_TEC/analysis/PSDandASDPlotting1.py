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

# 计算ASD
asd = np.sqrt(psd)

# 创建一个页面上的两个子图
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 12))

# 绘制PSD图
ax1.loglog(frequencies, psd, label='PSD')
ax1.set_xlabel('Frequency (Hz)', fontsize=20)
ax1.set_ylabel('PSD ($K^2/Hz$)', fontsize=20)
ax1.set_title('Power Spectral Density', fontsize=20)
ax1.legend(fontsize=20)
ax1.grid(True, which='both', linestyle='--')
ax1.tick_params(axis='both', which='major', labelsize=18)

# 绘制ASD图
ax2.loglog(frequencies, asd, label='ASD')
ax2.set_xlabel('Frequency (Hz)', fontsize=20)
ax2.set_ylabel('ASD ($K/\\sqrt{Hz}$)', fontsize=20)
ax2.set_title('Amplitude Spectral Density', fontsize=20)
ax2.legend(fontsize=20)
ax2.grid(True, which='both', linestyle='--')
ax2.tick_params(axis='both', which='major', labelsize=18)

# 调整布局以防止标题和标签重叠
plt.tight_layout(pad=3.0)
plt.subplots_adjust(hspace=0.4)  # 增加子图之间的垂直间距

# 展示图像
plt.show()
