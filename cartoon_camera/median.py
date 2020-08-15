#영상의 잡음
# 영상의 픽셀 값에 추가되는 원치 않는 형태의 신호

# 잡음제거 방법1
# 미디언 필터
# 주변 픽셀들의 값들을 정렬하여 그 중앙값으로 픽셀 값을 대체
# 소금-후추 잡음 제거에 효과적 
import sys
import numpy as np
import cv2

src = cv2.imread('.\cartoon_camera.\\noise.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.medianBlur(src, 3) #미디언 필터(3 x 3)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
