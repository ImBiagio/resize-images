from PIL import Image
import glob
import sys

path = sys.argv[1]

print (path+ "/?.jpg")

for name in glob.glob(path + "/*.jpg"):
    print (name)
    image = Image.open(name)
    image.thumbnail((2000, 2000))
    image.save(name)
    print(image.size)