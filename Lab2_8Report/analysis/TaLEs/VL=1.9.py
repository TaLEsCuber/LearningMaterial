import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.signal import find_peaks, peak_prominences

from matplotlib.ticker import ScalarFormatter, FormatStrFormatter

# 从Excel文件中读取数据
df = pd.read_excel('data1_24-05-09_0854.xlsx')

# 假设数据中的列名为x和y
x = df['Untitled'].values
y = df['Untitled 1'].values

# 找到峰值
peaks, _ = find_peaks(y, prominence=0.1, height=100)  # prominence参数可调整峰值的阈值
prominences = peak_prominences(y, peaks)[0]
valleys, _ = find_peaks(-y, prominence=10, height=prominences.mean()*-1, width=1)  # 寻找谷值，设定height为谷值的高度均值的负值

# 已知的谷值
known_valley_x = 71  # 已知谷值的 x 坐标
known_valley_y = 191.728592 # 已知谷值的 y 坐标


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


# 输出峰值的横坐标
print("峰值的横坐标：")
for peak in peaks:
    print(f'{x[peak]:.2f}')

# 输出谷值的横坐标
print("\n谷值的横坐标：")
for valley in valleys:
    print(f'{x[valley]:.2f}')

# 输出已知的谷值的横坐标
print("\n已知的谷值的横坐标：")
print(f'{known_valley_x:.2f}')
