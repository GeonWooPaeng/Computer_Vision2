# 잡음 제거 방법
# 양방향 필터 
# 가우시안 필터를 양쪽 방향으로 2번 하는 것
# 엣지 부분은 자신과 비슷한 부분만 블러링 하기 때문에 에지 보존할 수 있다.
# sigma값이 커지면 시간이 오래 걸린다.

import sys
import numpy as np
import cv2

src = cv2.imread('.\cartoon_camera.\lenna.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()


# cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace, dst, borderType)을 사용할 때 parameter을 잘 줘야한다.
# d: 필터링에 사용될 이웃 픽셀의 거리(지름)으로 음수(-1)를 입력하면 sigmaSpace 값에 의해 자동 결정된다.
# sigmaColor, sigmaSpace: 에지를 판단하는 것을 결정지을 수 있는 값
dst = cv2.bilateralFilter(src, -1, 10, 5) #sigmaColor: 10 ~ 20, sigmaSpace: 5 under

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
