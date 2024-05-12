import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.signal import find_peaks, peak_prominences


from matplotlib.ticker import ScalarFormatter, FormatStrFormatter

# 从Excel文件中读取数据
# df = pd.read_excel('data1_24-05-09_0918.xlsx')
df = pd.read_excel('手测.xlsx')



x = np.array(df['电压/V'])
y = -np.array(df['电流/A'])


# 找到峰值
peaks, _ = find_peaks(y, prominence=0.1, height=100)  # prominence参数可调整峰值的阈值
prominences = peak_prominences(y, peaks)[0]
valleys, _ = find_peaks(-y, prominence=10, height=prominences.mean()*-1, width=1)  # 寻找谷值，设定height为谷值的高度均值的负值

# 已知的谷值
known_valley_x = 70  # 已知谷值的 x 坐标
known_valley_y = 208 # 已知谷值的 y 坐标


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

plt.plot(x[peaks], y[peaks], "rx", label="Peaks")
plt.plot(x[valleys], y[valleys], "bo", label="Valleys")

plt.plot(known_valley_x, known_valley_y, "bo", label="Valleys")

plt.title('$V_L=1.9V$')
plt.xlabel('$V_{G_2K}/V$')
plt.ylabel('$I_P/10^{-11}A$')

# 在峰值旁边标注横纵坐标
for i in peaks:
    plt.text(x[i]-1, y[i]+3, f'({x[i]:.2f}, {y[i]:.2f})', color='red', ha='center')
for i in valleys:
    plt.text(x[i]-1, y[i]-20, f'({x[i]:.2f}, {y[i]:.2f})', color='blue', ha='center')

# 手动标注已知的谷值
plt.text(known_valley_x-1, known_valley_y-20, f'({known_valley_x:.2f}, {known_valley_y:.2f})', color='blue', ha='center')


plt.show()
