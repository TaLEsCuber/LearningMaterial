# import pandas as pd
# import matplotlib.pyplot as plt
# from datetime import datetime
#
# # 读取Excel文件
# df = pd.read_excel('黑面1.xlsx')
#
# # 获取时间列
# times = df['Time']
#
# # 转换为时间戳
# timestamps = [datetime.strptime(str(time).split('.')[0], "%Y-%m-%d %H:%M:%S") for time in times]
#
# # 计算每个时间戳对应的秒数
# seconds = [(timestamp - timestamps[0]).total_seconds() for timestamp in timestamps]
#
# # 绘制折线图
# plt.plot(seconds, df['Untitled'], linewidth=4)  # 将 'Column2' 替换为实际的第二列数据名称
# plt.xlabel('Time (seconds)')
# plt.ylabel('Temperature(℃)')
# # plt.title('Line Plot of Data')
# plt.show()






import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# 设置全局字号大小和图像尺寸
plt.rcParams.update({
    'font.size': 12,
    'axes.titlesize': 20,
    'axes.labelsize': 24,
    'xtick.labelsize': 20,
    'ytick.labelsize': 20,
    'legend.fontsize': 20,
    'figure.figsize': (8.27, 11.69)
})


# 读取Excel文件
df = pd.read_excel('黑面1.xlsx')

# 获取时间列
times = df['Time']

# 转换为时间戳
timestamps = [datetime.strptime(str(time).split('.')[0], "%Y-%m-%d %H:%M:%S") for time in times]

# 计算每个时间戳对应的秒数
seconds = [(timestamp - timestamps[0]).total_seconds() for timestamp in timestamps]

# 计算要保留的数据范围
num_points = len(seconds)
start_index = num_points // 3  # 开始位置为数据长度的1/3处
end_index = num_points  # 结束位置为数据末尾

# 绘制折线图
plt.plot(seconds[start_index:end_index], df['Untitled'][start_index:end_index], linewidth=4)  # 将 'Column2' 替换为实际的第二列数据名称
plt.xlabel('Time (seconds)')
plt.ylabel('Temperature(℃)')
# plt.title('Line Plot of Data (Last 2/3)')
plt.show()
