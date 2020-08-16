# 이미지 피라미드 
# 하나의 영상에 대해 다양한 크기의 해상도 영상 세트를 구성한 것
# 보통 가우시안 블러링 & 다운 샘플링 형태로 축소하여 구성 => 원하는 부분을 나타내기 위해 
# 다운 샘플링 -> 크기를 줄이는 것 
# 업샘플링 -> 크기를 늘리는 것(원래로 돌아가는 것)

#-----------------------------------------------
# 다운 샘플링 - cv2.pyrDown(src)
# 먼저 5 x 5 크기의 가우시안 필터를 적용(좀더 자연스러워 진다.)
# 이후 짝수 행과 열을 제거하여 작은 크기의 영상을 생성

# 업 생플링 - cv2.pyrUp(src)

import sys
import numpy as np
import cv2


src = cv2.imread('.\document_scanner.\cat.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()


rc = (250, 120, 200, 200)  # rectangle tuple

# 원본 영상에 그리기
cpy = src.copy()
cv2.rectangle(cpy, rc, (0, 0, 255), 2) # rc위치에 빨간색으로 두께가 2pixel을 그려준다.
cv2.imshow('src', cpy)
cv2.waitKey()

# 피라미드 영상에 그리기
for i in range(1, 4):
    src = cv2.pyrDown(src)
    cpy = src.copy()
    cv2.rectangle(cpy, rc, (0, 0, 255), 2, shift=i) #shift는 가로 세로를 얼마큼 줄일 것인지 나타내는 것
    cv2.imshow('src', cpy)
    cv2.waitKey()
    cv2.destroyWindow('src') #잔상을 없애주는 것

cv2.destroyAllWindows()
