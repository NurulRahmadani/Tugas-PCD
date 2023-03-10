from PIL import Image
from PIL import ImageFilter


def applyMaximumFilter(image):
    return image.filter(ImageFilter.MaxFilter)


imagePath = "nunu2.jpg"
imageObject = Image.open(imagePath)

filterApplied = imageObject
for i in range(0, 25):
    filterApplied = applyMaximumFilter(filterApplied)

imageObject.show()
filterApplied.show()