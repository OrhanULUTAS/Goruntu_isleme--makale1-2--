import cv2 as cv

img = cv.imread ("siyahbeyaz.jpg",0)
img_yukseklik = img.shape[0]
img_genislik = img.shape[1]
cv.imshow("original",img)
cv.waitKey()

for x in range (0,img_yukseklik):
    for y in range (0,img_genislik):
        img[x][y] = 256-img[x][y]
cv.imshow("inverted",img)
cv.waitKey()