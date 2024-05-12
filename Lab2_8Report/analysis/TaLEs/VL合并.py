import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 读取第一个Excel文件的数据
# VL=1.9V
df1 = pd.read_excel('data1_24-05-09_0854.xlsx')
x1 = np.array(df1['Untitled'])
y1 = np.array(df1['Untitled 1'])*10**-11


# 读取第二个Excel文件的数据
# VL=2.3V
df2 = pd.read_excel('data1_24-05-09_0918.xlsx')
x2 = np.array(df1['Untitled'])
y2 = np.array(df1['Untitled 1'])*10**-10

# 读取第三个Excel文件的数据
# VL=1.5V
df3 = pd.read_excel('data1_24-05-09_0927.xlsx')
x3 = df3['Untitled']
y3 = df3['Untitled 1']*10**-12



plt.rcParams.update({
    'font.size': 12,
    'axes.titlesize': 20,
    'axes.labelsize': 24,
    'xtick.labelsize': 20,
    'ytick.labelsize': 20,
    'legend.fontsize': 20,
})


# 绘制图像
plt.figure(figsize=(10, 6))
plt.plot(x1, y1, label='$V_L=1.9V$')
plt.plot(x2, y2, label='$V_L=2.3V$')
plt.plot(x3, y3, label='$V_L=1.5V$')
plt.xlabel('$V_{G_2K}/V$')
plt.ylabel('$I_P/10^{-8}A$')
plt.title('Influence of Different Filament Voltages on Curves')
plt.legend()
plt.show()
