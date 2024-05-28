import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件中的数据
file_path = 'P_3.xlsx'  # 请将此路径替换为你的Excel文件路径

# 使用pandas读取Excel文件
data = pd.read_excel(file_path)

# 假设你的数据有两列，分别是时间和温度
time = data['时间 - 曲线 0']
temperature = data['幅值 - 曲线 0']

# 绘制时域图
plt.figure(figsize=(16, 6))
plt.plot(time, temperature, label='Temperature')

# 设置横纵轴标签，标题和图例的字号大小
plt.xlabel('Time (s)', fontsize=20)  # 设置x轴标签的字号
plt.ylabel('Temperature (K)', fontsize=20)  # 设置y轴标签的字号
plt.title('Time Series Plot', fontsize=20)  # 设置标题的字号
plt.legend(fontsize=20)  # 设置图例的字号

# 设置横纵坐标轴刻度标签的字号
plt.xticks(fontsize=24)
plt.yticks(fontsize=24)

# 也可以使用tick_params函数进行更详细的设置
# plt.tick_params(axis='both', which='major', labelsize=12)

plt.grid(True)

# 保存图像，保持长宽比例不变
# plt.savefig('temperature_vs_time.png', bbox_inches='tight')

plt.show()
