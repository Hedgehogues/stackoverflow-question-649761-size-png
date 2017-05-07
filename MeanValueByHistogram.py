import Image
import os
import matplotlib.pyplot as plt
import numpy as np



def Model(a, x):
    sum = a[0]
    for coeff in range(1, len(a)):
        sum += a[coeff] * ((x * np.sin(x)) ** coeff + np.exp(x))
    return sum

listOfSize = []
listOfSizeTest = []
h = []
w = []
total = []
totalTest = []
data = []


index = 0
for itemFile in range(0, 250):
    img = Image.open("/home/hedgehogues/project/testPNG/" + str(index) + ".png")
    img.thumbnail((300, 300), Image.ANTIALIAS)
    img.save("/home/hedgehogues/project/testPNG/_-1.png")
    tmpSize = os.path.getsize("/home/hedgehogues/project/testPNG/_-1.png")
    img = np.array(img.convert('L'))
    y = np.histogram(img, bins = range(0, 256))
    total.append(np.mean(y[0] / float(np.max(y[0]))))
    index += 1



    print index

for itemFile in range(0, 6):

    img = Image.open("/home/hedgehogues/project/testPNG/_" + str(itemFile) + ".png")
    img.thumbnail((300, 300), Image.ANTIALIAS)
    img.save("/home/hedgehogues/project/testPNG/_-1.png")
    tmpSize = os.path.getsize("/home/hedgehogues/project/testPNG/_-1.png")
    img = np.array(img.convert('L'))
    listOfSizeTest.append(tmpSize)
    y = np.histogram(img, bins = range(0, 256))
    totalTest.append(np.mean(y[0] / float(np.max(y[0]))))


plt.plot(total, listOfSize, linestyle = '', marker = 'x')
plt.plot(totalTest, listOfSizeTest, linestyle = '', marker = 'x', color = 'red')
plt.show()