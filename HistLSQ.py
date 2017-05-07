import Image
import scipy.optimize as opt
import matplotlib.pyplot as plt
import numpy as np


# Целевая функция
def Model(a, x):
    sum = a[0]
    for coeff in range(1, len(a)):
        sum += a[coeff] * ((x * np.sin(x)) ** coeff + np.exp(x))
    return sum




index = 0
for itemFile in range(0, 250):
    img = Image.open("/home/hedgehogues/project/testPNG/" + str(index) + ".png")
    img.thumbnail((300, 300), Image.ANTIALIAS)
    img = np.array(img.convert('L'))
    weight = np.array(range(0, 10))
    ErrorFunc = lambda tpl, x, y: 0.5 * (Model(tpl, x) - y) ** 2 # Функционал минимизации
    y = np.histogram(img, bins = range(0, 256))
    x = np.arange(0, 1, 1./255) # Нормировка
    y = y[0] / float(np.max(y[0])) # Нормировка
    spl = opt.leastsq(ErrorFunc, weight, args = (x, y)) # Вычисление коэффициентов
    yy = Model(spl[0], x)
    plt.plot(x, yy)
    plt.plot(x, y)
    plt.show()
    index += 1



    print index