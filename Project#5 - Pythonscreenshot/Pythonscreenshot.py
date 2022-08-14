import pyscreenshot as ps
#Capture the image
image = ps.grab(bbox=(10, 10, 500, 500))

#Show the image
image.show()

image.save("Test.png")
