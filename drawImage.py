import numpy as np
import matplotlib.pyplot as plt
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


if __name__ == "__main__":
    kd = 0.00001
    m = 0.00001
    x_list = np.array([list(range(1, 81))])
    print(x_list)
    y_list1 = np.array([func1(e, kd, m) for e in x_list])
    y_list2 = np.array([func2(e, kd, m) for e in x_list])
    y_list3 = np.array([func3(e, kd, m) for e in x_list])
    # drawPic2(x_list, np.array([y_list1, y_list2, y_list3]))
