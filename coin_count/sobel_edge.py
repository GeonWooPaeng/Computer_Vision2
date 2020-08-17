# 영상의 그래디언트
# x방향의 미분과 y방향의 미분을 따로 계산후 합쳐서 계산한 것

#그래디언트 크기: 픽셀 값의 차이에 비례(픽셀 값이 얼마나 급격하게 변하고 있나)
#그래디언트 방향: 픽셀 값이 가장 급격하게 증가(밝아지는)하는 방향(픽셀 값이 가장 급격하게 변하고 있는 방향)

import sys
import numpy as np
import cv2


src = cv2.imread('.\coin_count.\lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dx = cv2.Sobel(src, cv2.CV_32F, 1, 0)
dy = cv2.Sobel(src, cv2.CV_32F, 0, 1)

mag = cv2.magnitude(dx, dy) #2D 벡터의 크기 계산 함수(결과: float형태)-> gray scale영상
mag = np.clip(mag, 0, 255).astype(np.uint8) #2D 벡터의 방향 계산 함수


#edge부분만 흰색으로 표현하는 edge영상 만들기
dst = np.zeros(src.shape[:2], np.uint8) #검정색으로 채워져 있는 edge영상
dst[mag > 120] = 255 #edge를 흰색으로 바꾸기
#_, dst = cv2.threshold(mag, 120, 255, cv2.THRESH_BINARY)

cv2.imshow('src', src)
cv2.imshow('mag', mag)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
