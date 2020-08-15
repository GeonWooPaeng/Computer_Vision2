# 전단 변환
# 층 밀림 변환, x축과 y축 방향에 대해 따로 정의

import sys
import numpy as np
import cv2


src = cv2.imread('.\document_scanner.\\tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

aff = np.array([[1, 0.5, 0],
                [0, 1, 0]], dtype=np.float32) # x' = x+0.5y, y' = y 

h, w = src.shape[:2]
dst = cv2.warpAffine(src, aff, (w + int(h * 0.5), h)) #밀려 나가는 것까지 보여주게 한 것

cv2.imshow('src', src)
cv2.imshow('dst', dst)

cv2.waitKey()
cv2.destroyAllWindows()
