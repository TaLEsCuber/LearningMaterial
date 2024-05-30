import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import fft

# 从Excel文件中读取数据
# 假设你的Excel文件名为'data.xlsx'，包含两个列't'和'omega'
df = pd.read_excel('PID_1.xlsx')

# 提取时间序列和角速度
t = df['时间 - 曲线 0'].values
omega = df['幅值 - 曲线 0'].values

# 计算时间间隔
dt = t[1] - t[0]

# 用FFT计算功率谱
power = np.abs(fft.fft(omega))**2
freq = fft.fftfreq(len(omega), dt)

# 作功率谱
fig, ax = plt.subplots(figsize=(14,7))
ax.plot(freq, power)
ax.set_xlabel('f', fontsize=18)
ax.set_ylabel('Power', fontsize=18)
ax.set_xlim(0, freq.max())
ax.set_ylim(power.min(), 800)

plt.show()
