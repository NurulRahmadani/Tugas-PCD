import cv2
import numpy as np

# membaca gambar
img = cv2.imread('img1.jpeg')

# menambahkan noise Gaussian ke gambar
noise = np.zeros(img.shape, np.uint8)
cv2.randn(noise, (0,0,0), (50,50,50))
noisy_img = cv2.add(img, noise)

# menampilkan gambar asli dan gambar yang telah di-blur
cv2.imshow('Original Img', img)
cv2.imshow('Noisy Img', noisy_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
