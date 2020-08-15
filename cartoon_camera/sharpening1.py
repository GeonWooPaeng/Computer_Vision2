# 샤프닝
# 영상을 날카롭게 만들겠다

#방법1 
# 언샤프 마스크 필터링 
# 부드러워진 영상을 이용하여 날카로운 영상을 생성

#그레이스케일 샤프닝하기

import sys
import numpy as np
import cv2

src = cv2.imread('.\cartoon_camera.\\rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

blr = cv2.GaussianBlur(src, (0, 0), 2) #블러링 만들기(시그마: 2)

#샤프닝 만들기
dst = np.clip(2.0*src - blr, 0, 255).astype(np.uint8) 
# dst = cv2.addWeighted(src, 2, blr, -1, 0) #src의 2배에 blr을 빼준 것

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
