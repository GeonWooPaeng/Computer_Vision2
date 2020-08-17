# 영상 미분 => 에지를 구하기 위함

# 에지 
# 배경과 객체 , 객체와 객체의 경계
# 영상에서 픽셀의 밝기 값이 급격하게 변하는 부분 
# => 미분 값이 크게 나타나는 부분 검출

# 소벨 필터 => 1배 2배 1배

import sys
import numpy as np
import cv2


src = cv2.imread('.\coin_count.\lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# x방향 미분 결과
# kernel = np.array([[-1, 0, 1],
#                    [-2, 0, 2],
#                    [-1, 0, 1]], dtype= np.float32)
# dx = cv2.filter2D(src, -1, kernel, delta=128) 



# dx = cv2.Sobel(src, -1, 1, 0, delta=128) # x뱡향 미분 
# dy = cv2.Sobel(src, -1, 0, 1, delta=128) # y방향 미분

cv2.imshow('src', src)
cv2.imshow('dx', dx)
cv2.imshow('dy', dy)
cv2.waitKey()

cv2.destroyAllWindows()
