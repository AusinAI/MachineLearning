from PIL import Image

im = Image.open(r"mycar.jpeg")

im.show()

# Code for opening file
f = open("mycar.jpeg","r")
print(f.read())

