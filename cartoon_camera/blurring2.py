import sys
import numpy as np
import cv2

src = cv2.imread('.\cartoon_camera.\\rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

cv2.imshow('src', src)

for ksize in (3, 5, 7): # 3x3, 5x5, 7x7를 이용해서 블러링을 한다
    dst = cv2.blur(src, (ksize, ksize))

    desc = 'Mean: {}x{}'.format(ksize, ksize)
    cv2.putText(dst, desc, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                1.0, 255, 1, cv2.LINE_AA) #사진에 표현을 해주는 것

    cv2.imshow('dst', dst)
    cv2.waitKey()

cv2.destroyAllWindows()
