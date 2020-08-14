# 블러링 효과 1
# 부드러워지는 효과

# 평균값 필터(Mean filter)
# 영상의 특정 좌표 값을 주변 픽셀 값들의 산술 평균으로 설정
# 픽셀 간의 그레이스케일 값의 급격한 변화가 줄어들어 부드러워지고, 영상에 있는 잡음 영향이 사라지는 효과
# 마스크가 늘어나면 연산량이 크게 증가 한다.

# 단점
# 모든 픽셀에 같은 가중치를 사용하여 평균을 계산
# 멀리 있는 픽셀의 영향을 많이 받을 수 있음

import sys
import numpy as np
import cv2


src = cv2.imread('.\cartoon_camera.\\rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

kernel = np.array([[1/9, 1/9, 1/9],
                   [1/9, 1/9, 1/9],
                   [1/9, 1/9, 1/9]], dtype = np.float32)
#kernel = np.ones((3, 3), dtype=np.float64) / 9.


dst = cv2.filter2D(src, -1, kernel) # 필터링 함수

# 3 X 3 짜리를 블러링하는 함수
# dst = cv2.blur(src, (3, 3)) 

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
