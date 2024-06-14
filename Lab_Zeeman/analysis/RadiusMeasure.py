import cv2
import numpy as np
from scipy.optimize import least_squares

# 用于存储选定点的列表
points = []
zoom_factor = 2  # 放大倍数

def calculate_circle(points):
    """ 通过选定的三个点计算圆心和半径 """
    def calc_R(c):
        """ 计算点到圆心 (c[0], c[1]) 的距离 """
        return np.sqrt((points[:, 0] - c[0])**2 + (points[:, 1] - c[1])**2)

    def f_2(c):
        """ 计算到圆心的距离差的平方和 """
        Ri = calc_R(c)
        return Ri - Ri.mean()

    # 初始估计
    x_m = np.mean(points[:, 0])
    y_m = np.mean(points[:, 1])
    center_estimate = (x_m, y_m)
    result = least_squares(f_2, center_estimate)
    center_2 = result.x

    # 计算半径
    Ri = calc_R(center_2)
    R = Ri.mean()
    return center_2, R

def on_mouse(event, x, y, flags, param):
    global points
    global zoom_factor
    global zoom_window_open

    if event == cv2.EVENT_MOUSEMOVE:
        if zoom_window_open:
            # 放大区域并显示
            zoom_img = img[max(0, y-50):min(img.shape[0], y+50), max(0, x-50):min(img.shape[1], x+50)]
            zoom_img = cv2.resize(zoom_img, (0, 0), fx=zoom_factor, fy=zoom_factor)
            # 绘制光标
            cv2.line(zoom_img, (zoom_img.shape[1]//2 - 10, zoom_img.shape[0]//2),
                     (zoom_img.shape[1]//2 + 10, zoom_img.shape[0]//2), (255, 0, 0), 1)
            cv2.line(zoom_img, (zoom_img.shape[1]//2, zoom_img.shape[0]//2 - 10),
                     (zoom_img.shape[1]//2, zoom_img.shape[0]//2 + 10), (255, 0, 0), 1)
            cv2.imshow("Zoom", zoom_img)

    elif event == cv2.EVENT_LBUTTONDOWN:
        zoom_window_open = True
        # 显示放大镜窗口
        cv2.namedWindow("Zoom")
        cv2.moveWindow("Zoom", x + 50, y + 50)

    elif event == cv2.EVENT_LBUTTONUP:
        zoom_window_open = False
        cv2.destroyWindow("Zoom")
        # 添加点
        points.append((x, y))
        print(f"Point selected: {(x, y)}")
        cv2.circle(img, (x, y), 5, (0, 255, 0), -1)
        cv2.imshow("Image", img)

        # 如果已经选择了三个点，则计算圆
        if len(points) == 3:
            points_np = np.array(points)
            center, radius = calculate_circle(points_np)
            print(f"Circle center: {center}, radius: {radius}")
            cv2.circle(img, (int(center[0]), int(center[1])), int(radius), (255, 0, 0), 2)
            cv2.imshow("Image", img)
            points.clear()  # 清空点列表以便继续选择新的点

# 读取图像
img = cv2.imread("6.jpg")

# 初始放大镜窗口状态
zoom_window_open = False

# 显示图像并绑定鼠标事件
cv2.imshow("Image", img)
cv2.setMouseCallback("Image", on_mouse)

cv2.waitKey(0)
cv2.destroyAllWindows()
