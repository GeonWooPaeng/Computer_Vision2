# 회전 변환 
# 영상을 특정 각도 만큼 회전시키는 것(반시계 방향)
# x' = cos@*x + sin@*y
# y' = -sin@*x + cos@*y

import sys
import math
import numpy as np
import cv2

src = cv2.imread('.\\document_scanner.\\tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

rad = 20 * math.pi / 180 #20 -> 반시계방향으로 20도
aff = np.array([[math.cos(rad), math.sin(rad), 0],
                [-math.sin(rad), math.cos(rad), 0]], dtype=np.float32)

dst = cv2.warpAffine(src, aff, (0, 0)) #영상의 모든 좌표를 변환한다.

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
