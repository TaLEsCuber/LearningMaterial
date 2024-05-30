import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch

# 读取 Excel 文件中的数据
df = pd.read_excel('PID_1.xlsx')

# 假设 Excel 文件中有两列：time 和 temperature
time = df['时间 - 曲线 0'].values
temperature = df['幅值 - 曲线 0'].values

# 计算采样频率
sampling_interval = np.mean(np.diff(time))  # 平均采样间隔
sampling_frequency = 1 / sampling_interval  # 采样频率

# 使用 Welch 方法计算 PSD
frequencies, psd = welch(temperature, fs=sampling_frequency, nperseg=256)

# 计算 ASD
asd = np.sqrt(psd)

# 绘制 PSD 图（对数坐标）
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.loglog(frequencies, psd)
plt.title('Power Spectral Density (PSD)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('PSD (V²/Hz)')
plt.grid(True, which="both", ls="--")

# 绘制 ASD 图（对数坐标）
plt.subplot(2, 1, 2)
plt.loglog(frequencies, asd)
plt.title('Amplitude Spectral Density (ASD)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('ASD (V/√Hz)')
plt.grid(True, which="both", ls="--")

plt.tight_layout()
plt.show()
