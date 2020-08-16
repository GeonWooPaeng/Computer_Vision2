# 리매핑
# 영상의 특정 위치 픽셀을 다른 위치에 재배치하는 일반적인 프로세스
# cv2.remap(src, map1, map2, interpolation, dst, borderMode, borderValue)
# map1: 결과 영상의 (x,y)좌표가 참조할 입력 영상의 x좌표, 입력영상과 크기 같고 np.float32인 numpy.ndarray이다.
# map2: 결과 영상의 (x,y)좌표가 참조할 입력 영상의 y좌표
# borderMode: 가장자리 픽셀 확장방식(기본: cv2.BORDER_CONSTANT)
# borderValue: cv2.BORDER_CONSTANT일 때 사용할 상수 값(기본: 0)

import sys
import numpy as np
import cv2


src = cv2.imread('.\document_scanner.\\tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

h, w = src.shape[:2]

#np.indices는 행렬의 index값(x좌표값, y좌표값)을 행렬의 형태로 반환한다.
map2, map1 = np.indices((h, w), dtype=np.float32)
map2 = map2 + 10 * np.sin(map1 / 32) #영상이 출렁이게 만드는 코드

# print(map1[0:5, 0:5])# 츨력

#cv2.BORDER_DEFAULT은 검정색으로 된 영상부분을 가까운 부분의 색으로 채워진다.
dst = cv2.remap(src, map1, map2, cv2.INTER_CUBIC, borderMode=cv2.BORDER_DEFAULT)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
