import pandas as pd
import matplotlib.pyplot as plt
import glob

# 文件夹路径
folder_path = 'E:/Workspace/GPLabR/Lab_TEC/analysis'

# 获取文件夹中所有Excel文件的路径
excel_files = glob.glob(f'{folder_path}/*.xlsx')

# 遍历每个Excel文件，读取数据并绘制时序图
for file_path in excel_files:
    # 读取Excel文件
    df = pd.read_excel(file_path)

    # 假设时间列名为 'Time'，温度列名为 'Temperature'
    time = df['时间 - 曲线 0']
    temperature = df['幅值 - 曲线 0']

    # 从文件路径中提取文件名作为图表标题的一部分
    file_name = file_path.split('/')[-1]

    # 绘制时序图
    plt.figure()
    plt.plot(time, temperature, marker='o', linestyle='-', label=file_name)
    plt.title(f'Time vs Temperature - {file_name}')
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.legend()
    plt.grid(True)
    plt.show()
