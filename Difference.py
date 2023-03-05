from PIL import Image, ImageChops

# membaca gambar pertama
img1 = Image.open('img1.jpeg')

# membaca gambar kedua
img2 = Image.open('img2.jpeg')

# menghitung perbedaan antara dua gambar
diff = Image.eval(ImageChops.difference(img1, img2), lambda x: 255 if x != 0 else 0)

# menyimpan difference image sebagai file baru
diff.save('difference_image.jpg')

# menampilkan gambar pertama, gambar kedua, dan difference image
img1.show()
img2.show()
diff.show()
