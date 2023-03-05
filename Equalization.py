import cv2
import numpy as np
from matplotlib import pyplot as plt

# membaca gambar
img = cv2.imread('image1.jpg', 0)

# melakukan histogram equalization
equ = cv2.equalizeHist(img)

# menampilkan gambar asli dan hasil equalization
cv2.imshow('Original Image', img)
cv2.imshow('Equalized Image', equ)

# menampilkan histogram asli dan histogram hasil equalization
hist, bins = np.histogram(img.flatten(), 256, [0, 256])
plt.hist(img.flatten(), 256, [0, 256], color='r')
plt.xlim([0, 256])
plt.show()

hist, bins = np.histogram(equ.flatten(), 256, [0, 256])
plt.hist(equ.flatten(), 256, [0, 256], color='r')
plt.xlim([0, 256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
