#블러링 효과2

# 가우시안(정규분포) 필터
# 가까운 픽셀은 큰 가중치를, 멀리 있는 픽셀은 작은 가중치를 사용하여 평균값 계산

# 가우시안 함수의 특징 
# symmetric - 좌우 대칭하다(mean(평균,median = mode)기준)
# 면적의 총은 1이다. 

import sys
import numpy as np
import cv2

src = cv2.imread('.\cartoon_camera.\\rose.bmp', cv2.IMREAD_GRAYSCALE)

# cv2.GaussianBlur(src, ksize, sigmaX, dst, sigmaY, borderType)
# ksize를 주지말고 sigmaX를 주면 자동으로 생성된다. => (0,0)을 주자 
# 값을 주면 범위를 잘라서 조금 이상하다
# sigmaY값도 None을 그냥 준다.

dst = cv2.GaussianBlur(src, (0, 0), 3)
dst2 = cv2.blur(src, (7, 7))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.waitKey()

cv2.destroyAllWindows()
