import Image
import glob


listOfImages = glob.glob("/home/hedgehogues/project/testPNG/*.jpg")

index = 0
for itemFile in listOfImages:
    img = Image.open(itemFile)
    img.save("/home/hedgehogues/project/testPNG/" + str(index) + ".png")
    index += 1
    print index
