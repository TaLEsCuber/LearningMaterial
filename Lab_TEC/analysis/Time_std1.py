import pandas as pd
import numpy as np

# 读取Excel文件
file_path = 'PID_2.xlsx'  # 替换为你的Excel文件路径
df = pd.read_excel(file_path)

# 假设Excel文件中的列名分别为 'Time' 和 'Temperature'
temperature = df['幅值 - 曲线 0']

# 计算平均值和标准差
mean_temperature = np.mean(temperature)
std_temperature = np.std(temperature)

print(f"控制温度的平均值: {mean_temperature:.2f} °C")
print(f"控制温度的标准差: {std_temperature:.2f} °C")
