import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

# 定义一个函数来计算三点形成的圆的半径和圆心
def calculate_circle(p1, p2, p3):
    temp = p2[0] ** 2 + p2[1] ** 2
    bc = (p1[0] ** 2 + p1[1] ** 2 - temp) / 2
    cd = (temp - p3[0] ** 2 - p3[1] ** 2) / 2
    det = (p1[0] - p2[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p2[1])

    if abs(det) < 1.0e-6:
        return None

    # 圆心坐标
    cx = (bc * (p2[1] - p3[1]) - cd * (p1[1] - p2[1])) / det
    cy = ((p1[0] - p2[0]) * cd - (p2[0] - p3[0]) * bc) / det
    radius = np.sqrt((cx - p1[0]) ** 2 + (cy - p1[1]) ** 2)

    return cx, cy, radius

# 使用matplotlib打开图片并获取用户点击的三个点
def get_points(image_path):
    img = plt.imread(image_path)
    fig, ax = plt.subplots()
    ax.imshow(img)
    plt.title('Click on three points on the circle')

    # 放大镜效果
    scale_factor = 2.5  # 放大倍数
    x1, x2, y1, y2 = plt.axis()
    zoomed_inset = None  # 用于存储放大区域的轴对象

    def on_move(event):
        nonlocal zoomed_inset
        if event.inaxes == ax:
            x_center = event.xdata
            y_center = event.ydata
            if x_center is not None and y_center is not None:
                # Calculate the bounds ensuring they are positive
                x_left = max(x_center - (x2-x1)/(4*scale_factor), 0)
                y_bottom = max(y_center - (y2-y1)/(4*scale_factor), 0)
                width = min((x2-x1)/scale_factor, x2 - x_left)
                height = min((y2-y1)/scale_factor, y2 - y_bottom)

                # Remove the old zoomed inset if it exists
                if zoomed_inset is not None:
                    zoomed_inset.remove()

                # Create a new zoomed inset with the calculated bounds
                zoomed_inset = ax.inset_axes([x_left, y_bottom, width, height])
                zoomed_inset.imshow(img)
                zoomed_inset.set_xlim(x_center - (x2-x1)/(8*scale_factor), x_center + (x2-x1)/(8*scale_factor))
                zoomed_inset.set_ylim(y_center - (y2-y1)/(8*scale_factor), y_center + (y2-y1)/(8*scale_factor))
                zoomed_inset.axis('off')
                fig.canvas.draw_idle()

    fig.canvas.mpl_connect('motion_notify_event', on_move)
    points = plt.ginput(3)
    # 移除放大区域
    if zoomed_inset is not None:
        zoomed_inset.remove()
    plt.close(fig)
    return points

# 主程序
def main():
    image_path = input("Enter the image path: ")
    print("Starting program...")
    points = get_points(image_path)
    circle = calculate_circle(*points)

    if circle is not None:
        cx, cy, radius = circle
        diameter = radius * 2
        print(f"The diameter of the circle is: {diameter:.2f}")
    else:
        print("The selected points do not form a circle.")

if __name__ == "__main__":
    main()
