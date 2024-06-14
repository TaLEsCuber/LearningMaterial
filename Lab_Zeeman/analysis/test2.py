import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import os

# 全局变量
points = []
zoom_factor = 1.2
current_zoom = 1
center_x, center_y = 0, 0
dragging = False
drag_start_x, drag_start_y = 0, 0

# 读取图片
img_path = "E:/Workspace/GPLabR/Lab_Zeeman/analysis/3.png"
img = cv2.imread(img_path)

# 放大函数
def zoom_in(event):
    global current_zoom
    current_zoom *= zoom_factor
    update_image()

# 缩小函数
def zoom_out(event):
    global current_zoom
    current_zoom /= zoom_factor
    update_image()

# 更新显示的图片
def update_image():
    global ax, img, current_zoom, center_x, center_y
    height, width = img.shape[:2]
    new_height, new_width = int(height / current_zoom), int(width / current_zoom)
    center_x = np.clip(center_x, new_width // 2, width - new_width // 2)
    center_y = np.clip(center_y, new_height // 2, height - new_height // 2)
    x1, y1 = center_x - new_width // 2, center_y - new_height // 2
    x2, y2 = center_x + new_width // 2, center_y + new_height // 2
    cropped_img = img[y1:y2, x1:x2]
    ax.clear()
    ax.imshow(cv2.cvtColor(cropped_img, cv2.COLOR_BGR2RGB))
    for (x, y) in points:
        if x1 <= x <= x2 and y1 <= y <= y2:
            ax.plot((x - x1) / current_zoom, (y - y1) / current_zoom, 'ro')  # 在裁剪图像上绘制红色圆点
    plt.draw()

# 鼠标双击事件回调
def on_double_click(event):
    global points, img, center_x, center_y, current_zoom
    if event.dblclick and event.inaxes not in [ax_zoom_in, ax_zoom_out]:
        if event.inaxes:
            height, width = img.shape[:2]
            new_height, new_width = int(height / current_zoom), int(width / current_zoom)
            x1, y1 = center_x - new_width // 2, center_y - new_height // 2
            x = int(event.xdata * current_zoom) + x1
            y = int(event.ydata * current_zoom) + y1
            if len(points) < 3:
                points.append((x, y))
                update_image()
            if len(points) == 3:
                plt.close()
                calculate_circle_diameter(points)

# 鼠标按下事件回调
def on_mouse_press(event):
    global dragging, drag_start_x, drag_start_y
    if event.button == 1 and event.inaxes not in [ax_zoom_in, ax_zoom_out]:
        dragging = True
        drag_start_x, drag_start_y = event.xdata, event.ydata

# 鼠标移动事件回调
def on_mouse_move(event):
    global dragging, center_x, center_y, drag_start_x, drag_start_y
    if dragging and event.inaxes:
        dx = event.xdata - drag_start_x
        dy = event.ydata - drag_start_y
        center_x -= int(dx * current_zoom)
        center_y -= int(dy * current_zoom)
        drag_start_x, drag_start_y = event.xdata, event.ydata
        update_image()

# 鼠标释放事件回调
def on_mouse_release(event):
    global dragging
    if event.button == 1:
        dragging = False

# 计算圆心和半径
def calculate_circle_diameter(points):
    (x1, y1), (x2, y2), (x3, y3) = points
    A = np.array([
        [x1, y1, 1],
        [x2, y2, 1],
        [x3, y3, 1]
    ])
    B = np.array([
        [x1 ** 2 + y1 ** 2],
        [x2 ** 2 + y2 ** 2],
        [x3 ** 2 + y3 ** 2]
    ])
    C = np.linalg.det(A)
    D = -np.linalg.det(np.column_stack((B, A[:, 1:])))
    E = np.linalg.det(np.column_stack((A[:, 0], B, A[:, 2:])))
    F = -np.linalg.det(np.column_stack((A[:, :2], B)))

    if C == 0:
        print("选取的点不构成一个圆")
        return

    x0 = -D / (2 * C)
    y0 = -E / (2 * C)
    radius = np.sqrt((D ** 2 + E ** 2 - 4 * C * F) / (4 * C ** 2))

    print(f"圆心: ({x0:.7g}, {y0:.7g})")
    print(f"半径: {radius:.7g}")
    print(f"直径: {2 * radius:.7g}")

    # 绘制并保存带有标记点的图像
    marked_img = img.copy()
    for (x, y) in points:
        cv2.circle(marked_img, (x, y), 5, (0, 0, 255), -1)  # 在原始图像上绘制红色圆点
    base_name = os.path.basename(img_path)
    save_path = os.path.join(os.path.dirname(img_path), f"marked_{base_name}")
    cv2.imwrite(save_path, marked_img)
    print(f"已保存带有标记点的图像为 {save_path}")

if img is None:
    print(f"无法打开或读取文件: {img_path}")
else:
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.2)
    ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    # 放大和缩小按钮
    ax_zoom_in = plt.axes([0.81, 0.05, 0.1, 0.075])
    ax_zoom_out = plt.axes([0.7, 0.05, 0.1, 0.075])
    b_zoom_in = Button(ax_zoom_in, 'Zoom In')
    b_zoom_out = Button(ax_zoom_out, 'Zoom Out')
    b_zoom_in.on_clicked(zoom_in)
    b_zoom_out.on_clicked(zoom_out)

    # 设置鼠标事件
    fig.canvas.mpl_connect('button_press_event', on_mouse_press)
    fig.canvas.mpl_connect('motion_notify_event', on_mouse_move)
    fig.canvas.mpl_connect('button_release_event', on_mouse_release)
    fig.canvas.mpl_connect('button_press_event', on_double_click)

    plt.show()
