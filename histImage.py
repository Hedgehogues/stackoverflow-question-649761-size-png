import Image
import matplotlib.pyplot as plt
import numpy as np


index = 0
for itemFile in range(0, 250):
    img = Image.open("/home/hedgehogues/project/testPNG/" + str(index) + ".png")
    img.thumbnail((300, 300), Image.ANTIALIAS)
    img = np.array(img.convert('L'))
    y = np.histogram(img, bins = range(0, 256))
    x = np.arange(0, 1, 1./255)
    plt.plot(x, y[0])
    plt.show()
    index += 1



    print index
