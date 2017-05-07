import Image
import os
import matplotlib.pyplot as plt
import numpy as np


listOfSize = []
total = []


index = 0
for itemFile in range(0, 260):
    tmpSize = os.path.getsize("/home/hedgehogues/project/testPNG/" + str(index) + ".png")
    img = Image.open("/home/hedgehogues/project/testPNG/" + str(index) + ".png")
    hLocal, wLocal = img.size
    img = np.array(img.convert('L'))
    listOfSize.append(tmpSize)
    total.append(wLocal * hLocal)
    index += 1
    print index

plt.plot(total, listOfSize, linestyle = '', marker = 'x')
plt.show()