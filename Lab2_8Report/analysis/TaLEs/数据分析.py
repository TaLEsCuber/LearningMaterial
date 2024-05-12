import numpy as np

# 峰值电压数据
peak_voltage = [18, 29, 40, 52, 65, 78]
valley_voltage = [23 , 34 , 46 ,59 , 71]

# 计算相邻峰值电压之间的差值
Delta = []
for i in range(3):
    Delta.append((peak_voltage[i+3] - peak_voltage[i])/3)
for i in range(2):
    Delta.append((valley_voltage[i+3]-valley_voltage[i+1])/2)


print(Delta)

# 计算平均间隔和标准差
mean_interval = np.mean(Delta)
# 计算标准差
X = 0
for x in Delta:
    X += (x - mean_interval)**2

std_deviation = np.sqrt(X/3)


print("平均间隔：", mean_interval)
print("标准差：", std_deviation)