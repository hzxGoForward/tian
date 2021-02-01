import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# 估算kd和m参数


def func1(x, kd, m):
    x = x*np.pi/180
    cs = np.cos(x)
    mi = -pow(np.tan(x), 2)/pow(m, 2)
    up = pow(np.e, mi)/pow(cs, 5)
    return (kd*cs + (1-kd)*up)

# 估算kd和m参数


def func2(x, kd, m):
    x = x*np.pi/180
    cs = np.cos(x)
    mi = -pow(np.tan(x), 2)/pow(m, 2)
    up = pow(np.e, mi)/pow(cs, 5)
    return (kd*cs)


# 估算kd和m参数
def func3(x, kd, m):
    x = x*np.pi/180
    cs = np.cos(x)
    mi = -pow(np.tan(x), 2)/pow(m, 2)
    up = pow(np.e, mi)/pow(cs, 5)
    return (1-kd)*up


def drawPic(x_list, y_list):
    for tmp_list in y_list:
        line, = plt.plot(x_list, tmp_list)
    plt.show()
    return plt


def drawPic2(x_list, y_list, label_list):
    for i in range(len(x_list)):
        line, = plt.plot(x_list[i], y_list[i], label=label_list[i])
    plt.show()
    return plt


def draw3D(X, Y, Z):
    fig = plt.figure()  # 定义新的三维坐标轴
    ax3 = plt.axes(projection='3d')

    # 作图
    ax3.plot_surface(X, Y, Z, cmap='rainbow')
    # ax3.contour(X,Y,Z, zdim='z',offset=-2，cmap='rainbow)   #等高线图，要设置offset，为Z的最小值

    plt.xlabel("angle")
    plt.ylabel("kd")
    plt.show()


if __name__ == "__main__":

    m = 0.5
    kd = np.arange(0.1, 1, 0.01)
    xx = np.arange(1, 81, 1)

    X, Y = np.meshgrid(xx, kd)

    Z = (1-Y)*pow(np.e, -pow(np.tan(X*np.pi/180), 2) /
                  pow(m, 2))/pow(np.cos(X*np.pi/180), 5)

    draw3D(X, Y, Z)

    # print(x_list)
    # y_list1 = np.array([func1(e, kd, m) for e in x_list])
    # y_list2 = np.array([func2(e, kd, m) for e in x_list])
    # y_list3 = np.array([func3(e, kd, m) for e in x_list])
    # drawPic2(x_list, np.array([y_list1, y_list2, y_list3]))
